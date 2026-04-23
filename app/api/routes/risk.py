from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def calculate_risk(payload: dict):
    score = 0

    if not payload.get("encryption"):
        score += 40

    if not payload.get("authentication"):
        score += 30

    if payload.get("data_sensitivity") == "high":
        score += 30

    return {
        "risk_score": min(score, 100),
        "severity": "HIGH" if score > 60 else "MEDIUM" if score > 30 else "LOW"
    }