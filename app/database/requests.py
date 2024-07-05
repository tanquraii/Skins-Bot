from app.database.models import async_session
from app.database.models import User,Category,Skin
from sqlalchemy import select

async def set_user(tg_id:int)->None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id==tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))

async def get_category_item(category_id):
    async with async_session() as session:
        return await session.scalars(select(Skin).where(Skin.weapon == category_id))

async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Skin).where(Skin.id == item_id))
