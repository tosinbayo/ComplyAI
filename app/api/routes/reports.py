from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.db.models import Analysis

router = APIRouter()


@router.get("/")
def get_reports(db: Session = Depends(get_db)):
    return db.query(Analysis).all()