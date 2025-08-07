from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.jenkins_service.router import router as jenkins_router

app = FastAPI(
    title="Automated Ops Publishing Platform",
    description="A platform to automate software releases using Jenkins.",
    version="1.0.0",
)

# API routers
app.include_router(jenkins_router, prefix="/api")

# Serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", include_in_schema=False)
async def root():
    return FileResponse('static/index.html')
