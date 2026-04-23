from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine

# Direct router imports (production-safe)
from app.api.routes.auth import router as auth_router
from app.api.routes.risk import router as risk_router
from app.api.routes.reports import router as reports_router
from app.api.routes.ai_systems import router as ai_systems_router
from app.api.routes.assessments import router as assessments_router


app = FastAPI(title="ComplyAI")


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create DB tables (MVP only — later replace with Alembic migrations)
Base.metadata.create_all(bind=engine)


# Register routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(reports_router, prefix="/reports", tags=["Reports"])
app.include_router(risk_router, prefix="/risk", tags=["Risk"])
app.include_router(ai_systems_router, prefix="/ai-systems", tags=["AI Systems"])
app.include_router(assessments_router, prefix="/assessments", tags=["Assessments"])


@app.get("/")
def root():
    return {"message": "API running"}