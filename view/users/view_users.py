from fastapi import APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from models.users import model_user
router_users = APIRouter(prefix='/users', tags=['users','user','persons',])


@router_users.get('/',response_model=None)
async def view_all_users(async_session:async_sessionmaker[AsyncSession]):
    async with async_session() as session:
        async with session.begin():
            users = select(model_user.User)
    context = {"users":users}
    return context

