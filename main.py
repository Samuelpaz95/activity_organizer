from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from app import user

app = FastAPI()
app.include_router(user.router, prefix="/users")


@app.exception_handler(Exception)
def handle_exception(request, exc):
    if isinstance(exc, IntegrityError):
        detail = str(exc).split("\n")[1]
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"detail": detail})
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content={"detail": str(exc)})
