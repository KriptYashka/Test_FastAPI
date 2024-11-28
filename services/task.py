from typing import List

from repositories.task import TaskRepository
from schemas.task import Task


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def get_books(self) -> List[Task]:
        result = self.repository.get_tasks()
        return result

    def create_book(self) -> Task:
        result = self.repository.create_task()
        return result