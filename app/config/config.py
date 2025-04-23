# app/config.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Load biến từ file .env

# class Settings(BaseSettings):
#     DB_HOST: str = os.getenv("DB_HOST")
#     DB_PORT: int = os.getenv("DB_PORT")
#     DB_USERNAME: str = os.getenv("DB_USERNAME")
#     DB_PASSWORD: str = os.getenv("DB_PASSWORD")
#     DB_DATABASE: str = os.getenv("DB_DATABASE")

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_DATABASE: str
    REDIS_HOST: str
# DATABASE_URL = "mysql+aiomysql://root:12345@localhost/sakila"
    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+aiomysql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
    