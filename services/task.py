from typing import List

from repositories.task import TaskRepository
from schemas.task import STask


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def get_tasks(self) -> List[STask]:
        result = self.repository.get_tasks()
        return result

    def create_task(self, task: STask) -> STask:
        task_id = self.repository.get_next_id()
        result = self.repository.create_task(task_id, task)
        return result

    def update_task(self, task: STask) -> STask:
        result = self.repository.update_task(task)
        return result