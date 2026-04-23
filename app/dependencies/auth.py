from fastapi import Header, HTTPException
from jose import jwt

from app.core.config import SECRET_KEY, ALGORITHM
from app.core.security import create_access_token
from app.schemas import user

def get_current_user(authorization: str = Header(...)):
    token = create_access_token({
    "sub": user.email,
    "tenant_id": user.tenant_id,
    "role": user.role
})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {
        "email": payload["sub"],
        "tenant_id": payload["tenant_id"],
        "role": payload["role"]
    }
    except:
        raise HTTPException(status_code=403, detail="Invalid token")