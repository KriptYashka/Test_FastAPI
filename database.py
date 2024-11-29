from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from models.task import TaskOrm

engine = create_async_engine("sqlite+aiosqlite:///tasks.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
   async with engine.begin() as conn:
      await conn.run_sync(TaskOrm.metadata.create_all)


async def delete_tables():
   async with engine.begin() as conn:
      await conn.run_sync(TaskOrm.metadata.drop_all)