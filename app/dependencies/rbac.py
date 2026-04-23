from fastapi import Depends
from app.dependencies.auth import get_current_user
from app.core.rbac import has_permission


def require_permission(permission: str):
    def wrapper(user=Depends(get_current_user)):
        has_permission(user, permission)
        return user
    return wrapper