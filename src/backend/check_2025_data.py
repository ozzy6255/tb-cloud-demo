from sqlalchemy import create_engine, text
import urllib.parse
from database import SERVER, PORT, DATABASE, USERNAME, PASSWORD

def check_2025_volume():
    params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER},{PORT};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")
    URL = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = create_engine(URL)
    
    # List of expected 2025 tables based on previous schema dump
    tables = [
        "TBOutCodeRelation250101", "TBOutCodeRelation250102", "TBOutCodeRelation250103",
        "TBOutCodeRelation250201", "TBOutCodeRelation250202", "TBOutCodeRelation250203",
        "TBOutCodeRelation250301"
    ]
    
    total_rows = 0
    with engine.connect() as conn:
        print("📊 Checking 2025 Data Volume:")
        for t in tables:
            try:
                result = conn.execute(text(f"SELECT COUNT(*) FROM {t}"))
                count = result.scalar()
                print(f" - {t}: {count} rows")
                total_rows += count
            except Exception as e:
                print(f" - {t}: Table not found or error ({e})")
                
    print(f"\n✅ Total Est. 2025 Rows: {total_rows}")

if __name__ == "__main__":
    check_2025_volume()
