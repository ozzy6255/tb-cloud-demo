from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Product(Base):
    __tablename__ = "products"

    ProductId = Column(Integer, primary_key=True, index=True)
    ProductName = Column(String, index=True)

class LogisticsRecord(Base):
    __tablename__ = "logistics_records"

    Code = Column(String, primary_key=True, index=True)
    OutTime = Column(String)
    DealerName = Column(String)
    ProductName = Column(String)
    OrderNo = Column(String)
    # Add other columns if known, e.g. ProductCode
    # Legacy schema usually has more, but this is enough for testing
