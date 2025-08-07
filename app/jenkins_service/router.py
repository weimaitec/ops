from fastapi import APIRouter, Depends, Body
from fastapi.responses import PlainTextResponse
from typing import Any, Dict
from .client import JenkinsClient

router = APIRouter(
    prefix="/jenkins",
    tags=["jenkins"],
)


@router.get("/jobs")
def get_jobs(client: JenkinsClient = Depends(JenkinsClient)):
    """
    Get a list of all jobs from Jenkins.
    """
    return client.get_jobs()


@router.get("/jobs/{job_name}")
def get_job_info(job_name: str, client: JenkinsClient = Depends(JenkinsClient)):
    """
    Get detailed information for a specific job.
    """
    return client.get_job_info(job_name)


@router.post("/jobs/{job_name}/build")
def build_job(
    job_name: str,
    parameters: Dict[str, Any] = Body(None),
    client: JenkinsClient = Depends(JenkinsClient),
):
    """
    Trigger a build for a specific job.
    Build parameters can be passed in the request body.
    """
    return client.build_job(job_name, parameters)


@router.get("/jobs/{job_name}/builds/{build_number}")
def get_build_info(
    job_name: str, build_number: int, client: JenkinsClient = Depends(JenkinsClient)
):
    """
    Get information about a specific build of a job.
    """
    return client.get_build_info(job_name, build_number)


@router.get("/jobs/{job_name}/builds/{build_number}/log", response_class=PlainTextResponse)
def get_build_console_output(
    job_name: str, build_number: int, client: JenkinsClient = Depends(JenkinsClient)
):
    """
    Get the console output (log) for a specific build.
    """
    return client.get_build_console_output(job_name, build_number)
