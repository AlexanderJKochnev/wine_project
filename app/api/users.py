# api/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.users import User
from app.schemas.users import UserCreate, UserOut
from sqlalchemy.future import select

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.username
                                                  == user.username))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400,
                            detail="Username already registered")
    db_user = User(username=user.username,
                   surname=user.surname,
                   name=user.name)
    db_user.set_password(user.password)
    print(f"Hashed password: {db_user.hashed_password}")
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@router.get("/", response_model=list[UserOut])
async def read_users(skip: int = 0, limit: int = 100,
                     db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).offset(skip).limit(limit))
    users = result.scalars().all()
    return users
