from sqlalchemy.orm import Session
from .models import Log
from datetime import datetime, timedelta

def calculate_health(service_name: str, db: Session):
    logs = db.query(Log).filter(Log.service_name == service_name).all()

    if not logs:
        return {"status": "Down", "error_rate": 0, "avg_response_time": 0}

    total = len(logs)
    errors = len([log for log in logs if log.level == "ERROR"])

    error_rate = (errors / total) * 100

    avg_response = sum([log.response_time_ms for log in logs]) / total

    status = "Healthy"
    if error_rate > 20:
        status = "Degraded"
    if error_rate > 50:
        status = "Unhealthy"

    return {
        "status": status,
        "error_rate": round(error_rate, 2),
        "avg_response_time": round(avg_response, 2)
    }
