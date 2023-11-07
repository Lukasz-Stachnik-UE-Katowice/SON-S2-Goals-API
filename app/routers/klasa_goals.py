from pydantic import BaseModel

class Goals(BaseModel):
    id: str
    item: str
    progress: float = 0.0