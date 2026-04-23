from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.models import User
from app.dependencies.db import get_db
from app.core.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserLogin, UserCreate
from app.core.security import create_access_token

router = APIRouter()


@router.post("/register")
def register(email: str, password: str, db: Session = Depends(get_db)):
    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    return {"message": "User created"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 👇 THIS is where your code goes
    token = create_access_token({
        "sub": db_user.email,
        "role": db_user.role.name,   # RBAC role
        "tenant_id": db_user.tenant_id
    })
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }