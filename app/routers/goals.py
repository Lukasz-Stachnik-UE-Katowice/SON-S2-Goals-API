from uuid import UUID
from fastapi import APIRouter, HTTPException
from .klasa_goals import Goals

router = APIRouter()

goals = [Goals(id="1",item="Obiekt")]

@router.get("/goals", tags=["goals"])
async def get_goals() -> list[Goals]:
    # Here we want to return all goals in the database
    return goals


@router.get("/goals/{goal_id}", tags=["goals"])
async def get_goal(goals_id: str):
    # Here we want to return goal that user whant's to see the details of
    for goal in goals:
        if goal.id == goals_id:
            return [goal]
    raise HTTPException(status_code=404, detail="Item not found")


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
async def update_goal(goal_id: str, update_goal: Goals):
    for goal in list:
        if goal.id == goal_id:
            goal.description = update_goal.description
            return {"message": "Goal updated successfully"}
    return {"message": "Goal not found"}


@router.delete("/goals/{goal_id}", tags=["goals"])
async def delete_goal(goal_id: UUID):
    # Here we want to delete goal from the database, and return status
    return


@router.post("/goals/{goal_id}", tags=["goals"])
async def post_progress_goal(progress: float):
    # Here we want to update the progress with given on or by given value
    return
