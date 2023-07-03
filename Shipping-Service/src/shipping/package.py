from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    item_id: str
    name: str
    count: int

@dataclass
class Package:
    items: List[Item]
    shape: str
    weight: float
    length: float
    width: float
    height: float
    