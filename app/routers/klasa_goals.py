from pydantic import BaseModel

class Goals(BaseModel):
    id: str
    item: str