from uuid import UUID
from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

class Goal(BaseModel):
    id: str
    description: str

router = APIRouter()
list_of_goals = []  # Initialize an empty list to store the goals.

goal1 = Goal(id="1", description="One glass of water every morning")
goal2 = Goal(id="2", description="Night face routine")
list_of_goals.extend([goal1, goal2])



@router.get("/goals", tags=["goals"])
async def get_goals():
    # Here we want to return all goals in the database
    return []


@router.get("/goals/{goal_id}", tags=["goals"])
async def get_goal(goals_id: UUID):
    # Here we want to return goal that user whant's to see the details of
    return []


@router.get("/goals/{username}", tags=["goals"])
async def get_user_goals(username: str):
    # Here we want to return all goals in the database for given user
    return [{"goal": "Learn Python"}]


@router.post("/goals", tags=["goals"])
async def post_goal(
        goal):  # Here we need to add goal model that is going to be created https://fastapi.tiangolo.com/tutorial/body/
    # Here we want to add new goal to the database and return it back with status
    return ""


@router.put("/goals/{goal_id}", tags=["goals"])
async def update_goal(goal_id: str, update_goal: Goal):
    for goal in list_of_goals:
        if goal.id == goal_id:
            goal.description = update_goal.description
            return {"message": "Goal updated successfully"}
    return {"message": "Goal not found"}


@router.delete("/goals/{goal_id}", tags=["goals"])
async def delete_goal(goal_id: UUID):
    # Here we want to delete goal from the database, and return status
    return


@router.post("/goals/{goal_id}", tags=["goals"])
async def post_progress_goal(progress: float, goal_id: int): 
    list_of_goals[goal_id].progress += progress
    return {"New progress of {}. goal".format(goal_id), "{}".format(list_of_goals[goal_id].progress)}
