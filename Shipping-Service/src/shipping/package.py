from typing import List
from pydantic import BaseModel


class Item(BaseModel):
    item_id: str
    name: str
    count: int


class Package(BaseModel):
    items: List[Item]
    shape: str
    weight: float
    length: float
    width: float
    height: float
