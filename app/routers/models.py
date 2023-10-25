from pydantic import BaseModel
from uuid import UUID

class Goal(BaseModel):
        id: str
        item: str