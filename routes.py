from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Log
from .schemas import LogCreate
from .monitoring import calculate_health

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/logs")
def create_log(log: LogCreate, db: Session = Depends(get_db)):
    db_log = Log(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return {"message": "Log stored successfully"}

@router.get("/health/{service_name}")
def get_health(service_name: str, db: Session = Depends(get_db)):
    return calculate_health(service_name, db)
