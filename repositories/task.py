from typing import List
from sqlalchemy import select
from database import new_session
from models.task import TaskOrm
from schemas.task import STask

class TaskRepository:
   @classmethod
   async def create_task(cls, task: STask) -> STask:
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