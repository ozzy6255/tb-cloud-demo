from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Product(Base):
    __tablename__ = "TBProduct"
    
    # Assuming ProductId is PK
    ProductId = Column(Integer, primary_key=True, index=True)
    ProductName = Column(String)
    # Add other columns if known, e.g. ProductCode
    # Legacy schema usually has more, but this is enough for testing
