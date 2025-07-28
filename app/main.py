# main.py
from fastapi import FastAPI
from app.api import users, storage
from app.database import engine
from app.models.users import Base as UserBase
from app.models.storage import Base as StorageBase

app = FastAPI(title="MyApp API",
              description="API for mobile apps with admin panel")


# Создание таблиц (на практике — лучше через Alembic!)
@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(UserBase.metadata.create_all)
        await conn.run_sync(StorageBase.metadata.create_all)

app.include_router(users.router)
app.include_router(storage.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to MyApp API! Use /docs for API docs."}
