from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    API_V1_STR: str = "/api/v1"  # Vous pouvez définir une valeur par défaut ici.
    PROJECT_NAME: str = "Inventory Management System"

    class Config:
        env_file = ".env"

settings = Settings()
