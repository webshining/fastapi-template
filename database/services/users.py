from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User


async def get_users(session: AsyncSession) -> list[User]:
    res = await session.execute(select(User))
    return res.scalars().all()