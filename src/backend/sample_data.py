from sqlalchemy import create_engine, text
import urllib.parse
from database import SERVER, PORT, DATABASE, USERNAME, PASSWORD

def sample_data():
    params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER},{PORT};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")
    URL = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = create_engine(URL)
    
    with engine.connect() as conn:
        print("🔍 Checking a sample Outbound Code:")
        # Adjust table name to one that actually exists and has data if possible
        try:
            result = conn.execute(text("SELECT TOP 5 Code, OutId FROM TBOutCodeRelation231201"))
            for row in result:
                print(f" - Scan Code: {row.Code}, OutId: {row.OutId}")
        except Exception as e:
            print(f"Error reading partition table: {e}")

        print("\n📦 Checking Product Codes:")
        result = conn.execute(text("SELECT TOP 5 ProductId, ProductNo, OneLevelCode, ProductName FROM TBProduct"))
        for row in result:
            print(f" - PrdId: {row.ProductId}, No: {row.ProductNo}, Level1: {row.OneLevelCode}, Name: {row.ProductName}")

if __name__ == "__main__":
    sample_data()
