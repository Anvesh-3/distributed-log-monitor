from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, index=True)
    level = Column(String)
    message = Column(String)
    response_time_ms = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
