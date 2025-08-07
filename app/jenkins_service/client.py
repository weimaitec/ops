import jenkins
from fastapi import HTTPException, status
from app.config import settings


class JenkinsClient:
    def __init__(self):
        try:
            self.server = jenkins.Jenkins(
                settings.JENKINS_URL,
                username=settings.JENKINS_USERNAME,
                password=settings.JENKINS_PASSWORD,
                timeout=10,
            )
            # Check connection
            self.server.get_whoami()
        except jenkins.JenkinsException as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Could not connect to Jenkins: {e}",
            )

    def get_jobs(self):
        try:
            return self.server.get_jobs()
        except jenkins.JenkinsException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error fetching jobs from Jenkins: {e}",
            )

    def get_job_info(self, job_name: str):
        try:
            return self.server.get_job_info(job_name)
        except jenkins.NotFoundException:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Job '{job_name}' not found.",
            )
        except jenkins.JenkinsException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error fetching job info for '{job_name}': {e}",
            )

    def build_job(self, job_name: str, parameters: dict | None = None):
        try:
            queue_item_number = self.server.build_job(job_name, parameters=parameters)
            return {"queue_item_number": queue_item_number}
        except jenkins.NotFoundException:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Job '{job_name}' not found.",
            )
        except jenkins.JenkinsException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error building job '{job_name}': {e}",
            )

    def get_build_info(self, job_name: str, build_number: int):
        try:
            return self.server.get_build_info(job_name, build_number)
        except jenkins.NotFoundException:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Build #{build_number} for job '{job_name}' not found.",
            )
        except jenkins.JenkinsException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error fetching build info for '{job_name}' #{build_number}: {e}",
            )

    def get_build_console_output(self, job_name: str, build_number: int):
        try:
            return self.server.get_build_console_output(job_name, build_number)
        except jenkins.NotFoundException:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Build #{build_number} for job '{job_name}' not found.",
            )
        except jenkins.JenkinsException as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error fetching console output for '{job_name}' #{build_number}: {e}",
            )
