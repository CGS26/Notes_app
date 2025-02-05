from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, Session ,declarative_base
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
DATABASE_URL = "sqlite+aiosqlite:///./Notes.db"
 
engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()
 
async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
 
async def get_db() -> Session: # type: ignore
    db = SessionLocal()
    try:
        yield  db
    finally:
       await db.close()
 