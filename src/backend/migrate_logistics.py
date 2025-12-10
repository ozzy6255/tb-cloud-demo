from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, LogisticsRecord
from database import engine as sqlite_engine, SessionLocal
import urllib.parse
from database import SERVER, PORT, DATABASE, USERNAME, PASSWORD

# SQL Server Connection
params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER},{PORT};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")
SOURCE_URL = f"mssql+pyodbc:///?odbc_connect={params}"
source_engine = create_engine(SOURCE_URL)

def migrate_logistics():
    print("🚀 Starting Logistics Data Migration (2025)...")
    
    # 1. Create Table in SQLite
    Base.metadata.create_all(bind=sqlite_engine)
    db = SessionLocal()
    
    # 2. Define Source Tables (2025 Partitions)
    partitions = [
        "TBOutCodeRelation250101", "TBOutCodeRelation250102", "TBOutCodeRelation250103",
        "TBOutCodeRelation250201", "TBOutCodeRelation250202", "TBOutCodeRelation250203",
        "TBOutCodeRelation250301"
    ]
    
    total_migrated = 0
    
    for table in partitions:
        print(f"📦 Processing table: {table} ...")
        try:
            # Join Logic: Relation(OutId) -> TBOutOrder(OrderId) -> TBCustomer(CustomerId)
            # Note: Assuming OutId in Relation maps to OrderId in Order table
            sql = f"""
            SELECT TOP 10000
                R.Code,
                O.OutTime,
                C.CustomerName,
                O.OrderNo
            FROM {table} R
            LEFT JOIN TBOutOrder O ON R.OutId = O.OrderId
            LEFT JOIN TBCustomer C ON O.CustomerId = C.CustomerId
            """
            
            with source_engine.connect() as conn:
                result = conn.execute(text(sql))
                rows = result.fetchall()
                
                if not rows:
                    print(f"   ⚠️ No data found in {table}")
                    continue
                
                print(f"   Found {len(rows)} rows. Inserting...")
                
                for row in rows:
                    # Check if exists
                    existing = db.query(LogisticsRecord).filter(LogisticsRecord.Code == row.Code).first()
                    if not existing:
                        record = LogisticsRecord(
                            Code=row.Code,
                            OutTime=str(row.OutTime) if row.OutTime else "",
                            DealerName=row.CustomerName or "Unknown",
                            ProductName="Unknown Product", # Placeholder as link is missing
                            OrderNo=row.OrderNo or ""
                        )
                        db.add(record)
                        total_migrated += 1
                
                db.commit()
                
        except Exception as e:
            print(f"   ❌ Error processing {table}: {e}")
            
    print(f"✅ Migration Complete! Total records: {total_migrated}")
    db.close()

if __name__ == "__main__":
    migrate_logistics()
