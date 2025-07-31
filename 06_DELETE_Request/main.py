from fastapi import FastAPI, APIRouter
import uvicorn
from pydantic import BaseModel
import random


class User(BaseModel):
    id: int = None
    name: str
    profession: str


app = FastAPI()
router = APIRouter()

data = []


@router.get("/")
async def home():
    if data:
        return data
    return {"message": "api running"}


@router.post("/add-user")
async def add(user: User):
    user.id = random.randint(1000, 9999)
    data.append(user)
    return {"message": "user added succesfully", "user": user}


@router.put("/update-user/{userid}")
async def update(userid: int, user: User):
    for i in data:
        if i.id == userid:
            i.id = userid
            i.name = user.name
            i.profession = user.profession
            return {"message": "Person updated successfully"}


@router.delete("/delete-user/{userid}")
async def delete(userid: int):
    for i in data:
        if i.id == userid:
            data.remove(i)
            return {"message": "user removed successfully"}


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app)
