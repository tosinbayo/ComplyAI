from fastapi import HTTPException

def has_permission(user, permission: str):
    role = user["role"]

    role_permissions = {
        "admin": ["*"],  # full access
        "auditor": ["view_reports", "create_report", "run_ai_scan"],
        "user": ["view_reports", "run_ai_scan"],
    }

    allowed = role_permissions.get(role, [])

    if "*" in allowed or permission in allowed:
        return True

    raise HTTPException(status_code=403, detail="Insufficient permissions")