# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import users, storage   # NOQA: E402
from app.database import engine   # NOQA: E402
from app.models.users import Base as UserBase   # NOQA: E402
from app.models.storage import Base as StorageBase   # NOQA: E402
# from app.admin import setup_admin


app = FastAPI(title="Wine Shelf API",
              description="API for mobile apps with admin panel")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# setup_admin(app)


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
