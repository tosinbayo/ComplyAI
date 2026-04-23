from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.dependencies.rbac import require_permission
from app.services.ai_service import analyze_document
from app.services.report_service import save_report

router = APIRouter()


@router.post("/analyze")
async def analyze(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    result = analyze_document(text)

    record = save_report(db, file.filename, "ISO27001", result)

    return {"id": record.id, "analysis": result}


@router.post("/generate-report")
def generate_report(
    user=Depends(require_permission("create_report")),
    framework: str = "ISO 27001",
    document: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return {"message": "RBAC protected endpoint working"}