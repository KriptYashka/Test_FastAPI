from typing import List

from repositories.task import TaskRepository
from schemas.task import STask


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    async def get_tasks(self) -> List[STask]:
        result = await self.repository.get_tasks()
        return result

    async def create_task(self, task: STask) -> STask:
        result = await self.repository.create_task(task)
        return result