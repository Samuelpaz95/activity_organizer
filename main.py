from fastapi import FastAPI

from app import user

app = FastAPI()

app.include_router(user.router, prefix="/users")


@app.get("/")
def root():
    return {"message": "Hello World"}
