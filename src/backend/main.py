from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TBAnti Query API", description="Legacy DB Query Interface", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For learning/dev, allow all. In prod, specify ["http://localhost:8080"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to TBAnti Query API. Visit /docs for Swagger UI."}

from models import Product

@app.get("/products")
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(Product).order_by(Product.ProductId).offset(skip).limit(limit).all()
    return products

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Simple query to check DB connection
        result = db.execute(text("SELECT 1")).scalar()
        return {"status": "ok", "db_connected": result == 1}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
