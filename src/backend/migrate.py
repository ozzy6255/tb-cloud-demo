import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product
from database import SERVER, PORT, DATABASE, USERNAME, PASSWORD

def migrate():
    # 1. Setup Source (SQL Server)
    print("🚀 Connecting to Source: SQL Server...")
    params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER},{PORT};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")
    SOURCE_URL = f"mssql+pyodbc:///?odbc_connect={params}"
    source_engine = create_engine(SOURCE_URL)
    SourceSession = sessionmaker(bind=source_engine)

    # 2. Setup Destination (SQLite)
    print("📂 Connecting to Destination: SQLite (app.db)...")
    DEST_URL = "sqlite:///./app.db"
    dest_engine = create_engine(DEST_URL, connect_args={"check_same_thread": False})
    DestSession = sessionmaker(bind=dest_engine)

    # 3. Reset & Create Schema
    print("✨ Creating tables in SQLite...")
    Base.metadata.drop_all(bind=dest_engine) # Start fresh
    Base.metadata.create_all(bind=dest_engine)
    
    source_db = SourceSession()
    dest_db = DestSession()
    
    try:
        # 4. Fetch Data
        print("📥 Fetching products from SQL Server...")
        products = source_db.query(Product).all()
        count = len(products)
        print(f"✅ Found {count} products.")
        
        if count == 0:
            print("⚠️ No data found in source database. Migration skipped.")
            return

        # 5. Insert Data
        print(f"📤 Migrating {count} records to SQLite...")
        
        # Batch insert is faster, but simple loop is fine for <30k rows for now
        # Detach objects from source session by creating new instances
        # This prevents "Session is bound to different engine" errors
        for p in products:
            new_p = Product(
                ProductId=p.ProductId, 
                ProductName=p.ProductName
                # Add other fields here if models.py maps them
            )
            dest_db.add(new_p)
        
        dest_db.commit()
        
        # 6. Verify
        final_count = dest_db.query(Product).count()
        print(f"🎉 Migration successful! SQLite now has {final_count} records.")
        
    except Exception as e:
        print(f"❌ Error during migration: {str(e)}")
        dest_db.rollback()
    finally:
        source_db.close()
        dest_db.close()

if __name__ == "__main__":
    migrate()
