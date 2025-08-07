from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JENKINS_URL: str
    JENKINS_USERNAME: str
    JENKINS_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()
