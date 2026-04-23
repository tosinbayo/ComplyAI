from pydantic import BaseModel, EmailStr


# ----------------------
# REQUEST SCHEMAS
# ----------------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str


# ----------------------
# RESPONSE SCHEMA (OPTIONAL BUT PRO)
# ----------------------
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # for SQLAlchemy