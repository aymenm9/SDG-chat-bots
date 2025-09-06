from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Role(str, Enum):
    user = "user"
    model = "model"

class Msg(BaseModel):
    role: Role
    content: str
class Massage(BaseModel):
    summary: Optional[str]=None
    history: list[Msg]=Field(default_factory=list, max_items=9)
    message: str
    
