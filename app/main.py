from fastapi import FastAPI
from .routers import goals
from pydantic import BaseModel

app = FastAPI()

app.include_router(goals.router)

@app.get("/")
async def root():
    return {"message": "Hello Students!"}

@app.post("/")
async def post(goal: Goal):
    zmienna = 0
    return zmienna