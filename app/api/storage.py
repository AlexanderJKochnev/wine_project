# api/storage.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.storage import Storage
from app.schemas.storage import StorageCreate, StorageUpdate, StorageOut
from sqlalchemy.future import select

router = APIRouter(prefix="/storage", tags=["storage"])


@router.post("/", response_model=StorageOut)
async def create_storage(item: StorageCreate,
                         db: AsyncSession = Depends(get_db)):
    db_item = Storage(**item.dict())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


@router.get("/", response_model=list[StorageOut])
async def read_storage(skip: int = 0, limit: int = 100,
                       db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Storage).offset(skip).limit(limit))
    items = result.scalars().all()
    return items


@router.get("/{item_id}", response_model=StorageOut)
async def read_storage_item(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Storage).filter(Storage.id == item_id))
    item = result.scalars().first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=StorageOut)
async def update_storage(item_id: int, item: StorageUpdate,
                         db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Storage).filter(Storage.id == item_id))
    db_item = result.scalars().first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    await db.commit()
    await db.refresh(db_item)
    return db_item


@router.delete("/{item_id}")
async def delete_storage(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Storage).filter(Storage.id == item_id))
    db_item = result.scalars().first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    await db.delete(db_item)
    await db.commit()
    return {"status": "deleted"}
