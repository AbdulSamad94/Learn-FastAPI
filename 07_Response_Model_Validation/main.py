from fastapi import FastAPI, APIRouter
import uvicorn
from pydantic import BaseModel
from typing import List


class UserIn(BaseModel):
    first_name: str
    second_name: str
    age: int
    email: str
    password: str


class UserOut(BaseModel):
    first_name: str
    second_name: str
    email: str


app = FastAPI()
router = APIRouter()

users = []


@router.get("/", response_model=List[UserOut])
async def home():
    if users:
        return users
    return {"message": "hello world!"}


@router.get("/users")
async def get_details():
    if users:
        return users
    return {"message": "No users found!"}


@router.post("/add-user", response_model=UserOut)
async def add(user: UserIn):
    users.append(user)
    return user


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app)
