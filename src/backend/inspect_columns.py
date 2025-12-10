from sqlalchemy import create_engine, inspect
import urllib.parse
from database import SERVER, PORT, DATABASE, USERNAME, PASSWORD

def inspect_columns(table_names):
    params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER},{PORT};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")
    URL = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = create_engine(URL)
    inspector = inspect(engine)
    
    for table in table_names:
        print(f"\n📊 Columns in {table}:")
        try:
            columns = inspector.get_columns(table)
            for col in columns:
                print(f"  - {col['name']} ({col['type']})")
        except Exception as e:
            print(f"  ❌ Error: {e}")

if __name__ == "__main__":
    inspect_columns(["Order"])
