from fastapi import FastAPI

from app.user import user_router

app = FastAPI()

app.include_router(user_router, prefix="/users")


@app.get("/")
def root():
    return {"message": "Hello World"}
