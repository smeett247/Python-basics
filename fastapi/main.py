from fastapi import FastAPI
from database.database import Base, engine
from auth.auth import auth_router
from user.routes import user_router
import uvicorn

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI with PostgreSQL"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
