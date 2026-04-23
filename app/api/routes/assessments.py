from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_assessments():
    return {
        "message": "Assessments working",
        "data": []
    }