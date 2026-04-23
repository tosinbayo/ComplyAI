from app.db.models import Role, Permission

def seed_rbac(db):
    roles = ["admin", "auditor", "user"]

    permissions = [
        "create_report",
        "view_reports",
        "delete_report",
        "run_ai_scan",
        "manage_users"
    ]

    for r in roles:
        if not db.query(Role).filter_by(name=r).first():
            db.add(Role(name=r))

    for p in permissions:
        if not db.query(Permission).filter_by(name=p).first():
            db.add(Permission(name=p))

    db.commit()