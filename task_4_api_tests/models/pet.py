from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Category:
    id: int
    name: str

@dataclass
class Tag:
    id: int
    name: str   

@dataclass
class Pet:
    id: int
    category: Optional[Category]
    name: Optional[str]
    photoUrls: List[str]
    tags: List[Tag]
    status: str
