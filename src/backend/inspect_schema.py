import urllib.parse
from sqlalchemy import create_engine, inspect
from database import SERVER, PORT, DATABASE, USERNAME, PASSWORD

def list_tables():
    print(f"🕵️‍♀️ Inspecting database: {DATABASE}")
    try:
        params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER},{PORT};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")
        URL = f"mssql+pyodbc:///?odbc_connect={params}"
        engine = create_engine(URL)
        inspector = inspect(engine)
        
        tables = inspector.get_table_names()
        print(f"✅ Found {len(tables)} tables:")
        for table in tables:
            print(f" - {table}")
            
    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    list_tables()
