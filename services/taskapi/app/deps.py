from fastapi import Depends
from app.db import AsyncSession

async def get_session() -> AsyncSession: