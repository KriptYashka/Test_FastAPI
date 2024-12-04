from typing import List, Optional

from repositories.task import TaskRepository
from schemas.task import STask, STaskBody


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def get_tasks(self) -> List[STask]:
        result = self.repository.get_tasks()
        return result

    def get_task_by_id(self, task_id: str) -> Optional[STask]:
        result = self.repository.get_task_by_id(task_id)
        return result

    def get_task_by_category(self, category: str) -> List[STask]:
        result = self.repository.get_tasks_by_category(category)
        return result

    def create_task(self, task: STaskBody) -> STask:
        task_id = self.repository.get_next_id()
        result = self.repository.create_task(task_id, task)
        return result

    def update_task(self, task_id: str, task: STaskBody) -> Optional[STask]:
        result = self.repository.update_task(task_id, task)
        return result

    def update_done_task(self, task_id: str) -> Optional[STask]:
        result = self.repository.update_done_task(task_id)
        return result

    def delete_task(self, task_id: str) -> dict:
        is_deleted = self.repository.delete_task(task_id)
        response = {"status": "OK"}
        if not is_deleted:
            response["status"] = f"Task ID {task_id} not exists."
        return response
