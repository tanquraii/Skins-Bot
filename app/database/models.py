from sqlalchemy import BigInteger,String,ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs,async_sessionmaker,create_async_engine

engine = create_async_engine(url = 'sqlite+aiosqlite:///cal.sqlite3')
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs,DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key = True)
    tg_id = mapped_column(BigInteger)

class Category(Base):#this is the model
    __tablename__ = 'weapons'#this is the name of the model
    id:Mapped[int] = mapped_column(primary_key=True)#this is one column of the model
    name:Mapped[str] = mapped_column(String(25))#this is the name of the category

class Skin(Base):
    __tablename__ = 'skins'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(primary_key=True)
    price:Mapped[int] = mapped_column(primary_key=True)
    weapon:Mapped[int] = mapped_column(ForeignKey('weapons.id'))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)#creates the database