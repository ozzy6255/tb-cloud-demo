from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from pathlib import Path
import models

app = FastAPI(title="TB Logistics Query API", description="Product & Logistics Tracking System", version="2.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (Vue frontend)
static_dir = Path("/app/static")
if static_dir.exists():
    app.mount("/assets", StaticFiles(directory=str(static_dir / "assets")), name="assets")

# API Routes
@app.get("/api")
def read_root():
    return {"message": "TB Logistics API v2.0 - Visit /docs for Swagger UI"}

@app.get("/api/products")
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

@app.get("/api/logistics")
def get_logistics(code: str, db: Session = Depends(get_db)):
    record = db.query(models.LogisticsRecord).filter(models.LogisticsRecord.Code == code).first()
    if not record:
        raise HTTPException(status_code=404, detail="Logistics record not found")
    return record

@app.get("/api/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Catch-all route for Vue SPA (must be last)
@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
    """Serve Vue SPA for all non-API routes"""
    index_file = static_dir / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return {"message": "Frontend not deployed. API available at /api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
