import os
import uuid
from fastapi import APIRouter

router = APIRouter()

@router.get("/hostname")
def get_hostname():
    return {"hostname": os.uname().nodename}

@router.get("/author")
def get_author():
    author_name = os.getenv("AUTHOR", "Unknown")
    return {"author": author_name}

@router.get("/id")
def get_id():
    return {"id": str(uuid.uuid4())}