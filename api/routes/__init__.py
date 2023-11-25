from fastapi import APIRouter, Depends

from database.models.base import get_session
from database.services import get_users

router = APIRouter()


@router.get('/')
async def root(session=Depends(get_session)):
    return {"users": await get_users(session)}
