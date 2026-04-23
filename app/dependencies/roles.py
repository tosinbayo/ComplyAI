from fastapi import HTTPException

def require_role(required_role: str):
    def role_checker(user):
        if user["role"] != required_role:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    return role_checker