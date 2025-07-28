# config.py загрузка переменных
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# загрузка переменных окружения

load_dotenv()


class Settings(BaseSettings):
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = os.getenv("API_PORT", 8000)
    sources = ['postgresql+asyncpg://', 'POSTGRES_USER', ':',
               'POSTGRES_PASSWORD', '@', 'POSTGRES_HOST', '/',
               'POSTGRES_DB']
    database_url: str = ''.join(os.getenv(a, a) for a in sources)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
