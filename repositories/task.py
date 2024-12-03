from typing import List
from sqlalchemy import select, update, delete
from database import new_session
from models.task import TaskOrm
from schemas.task import STask


class TaskRepository:
    @classmethod
    async def create_task(cls, task: STask) -> TaskOrm:
        async with new_session() as session:
            data = task.model_dump()
            new_task = TaskOrm(**data)
            session.add(new_task)
            await session.flush()
            await session.commit()
            return new_task

    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            tasks = [task_model for task_model in task_models]
            return tasks

    @classmethod
    async def get_task(cls, obj_id: int):
        async with new_session() as session:
            query = select(TaskOrm).where(TaskOrm.id == obj_id)
            result = await session.execute(query)
            task = result.scalars().first()
            return task

    @classmethod
    async def update_task(cls, task: STask) -> STask:
        async with new_session() as session:
            data = task.model_dump()
            del data["id"]
            query = update(TaskOrm).where(TaskOrm.id == task.id).values(**data)
            # print(task.model_dump())
            result = await session.execute(query)
            await session.commit()
            print(result)
            return task