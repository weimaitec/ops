from fastapi import FastAPI
from app.jenkins_service.router import router as jenkins_router

app = FastAPI(
    title="Automated Ops Publishing Platform",
    description="A platform to automate software releases using Jenkins.",
    version="1.0.0",
)

app.include_router(jenkins_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Automated Ops Publishing Platform"}
