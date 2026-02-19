from pydantic import BaseModel

class LogCreate(BaseModel):
    service_name: str
    level: str
    message: str
    response_time_ms: int
