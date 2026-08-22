from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config import Settings

settings = Settings()
engine = create_async_engine(settings.database_url, pool_size=10)
session = async_sessionmaker(engine, expire_on_commit=False)
