from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def users():
    return [{
        "email": "fulano.mengano@supermail.com",
        "first_name": "Fulano",
        "last_name": "Mengano",
        "username": "fulano123"
    }]
