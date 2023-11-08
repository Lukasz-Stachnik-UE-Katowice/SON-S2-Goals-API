from pydantic import BaseModel

class Goal(BaseModel):
    id: str
    due_date: str
    frequency: str