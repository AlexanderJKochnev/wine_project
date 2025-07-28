# schemas/storage.py
from pydantic import BaseModel


class StorageBase(BaseModel):
    name: str
    description: str | None = None


class StorageCreate(StorageBase):
    pass


class StorageUpdate(StorageBase):
    pass


class StorageOut(StorageBase):
    id: int

    class Config:
        from_attributes = True
