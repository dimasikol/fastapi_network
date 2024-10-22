import asyncio

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from models.app.model_default import BaseModel
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///../database.db"

metadata_obj = MetaData()
engine = create_async_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
BaseModel.metadata.create_all(bind=engine)

async def async_create_db():
    async with engine.begin() as conn:
        await conn.run_sync()

asyncio.run(async_create_db())


#SessionLocal = async_session_maker(autoflush=False, bind=engine)

#async def get_db():
#    db = SessionLocal
#    try:
#        yield db
#    finally:
#       db.close()
