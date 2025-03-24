from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn



app = FastAPI()

users = []
class User(BaseModel):
    name: str
    age: int



@app.get("/users")
def get_users():
    return {"users": users}


@app.post("/users")

def create_user(user: User):
    users.append(user.model_dump())
    return{"message": f"user {user.name} added successfully"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)