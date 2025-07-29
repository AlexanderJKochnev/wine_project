# config.py загрузка переменных
from dotenv import load_dotenv
import os

# загрузка переменных окружения

load_dotenv()


class Settings:
    sources: list = ['postgresql+asyncpg://', 'POSTGRES_USER', ':',
                     'POSTGRES_PASSWORD', '@', 'POSTGRES_HOST', '/',
                     'POSTGRES_DB']
    database_url: str = ''.join(os.getenv(a, a) for a in sources)
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", 8000))


settings = Settings()
