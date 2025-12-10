from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib.parse

import os

# Connection Config
# NOTE: Drivers for Mac (ODBC Driver 17 for SQL Server) must be installed via Homebrew.
# brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
# brew update
# brew install msodbcsql17 mssql-tools

SERVER = "localhost"
PORT = "1433"
DATABASE = "TB_Restored"
USERNAME = "sa"
PASSWORD = "MyNewPass123"

DB_TYPE = os.getenv("DB_TYPE", "mssql")

if DB_TYPE == "sqlite":
    SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
    # connect_args={"check_same_thread": False} is needed for SQLite in multithreaded apps like FastAPI
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    # Encode password to handle special characters
    params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER},{PORT};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}")
    SQLALCHEMY_DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
