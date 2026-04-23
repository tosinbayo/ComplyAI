from app.db.models import Analysis


def save_report(db, filename, framework, result):
    record = Analysis(
        filename=filename,
        framework=framework,
        result=result
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record