from fastapi import FastAPI
from .database import engine, Base
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Distributed Log Monitoring Service")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Log Monitoring Service Running"}
