"""
Файл внедрения зависимостей
"""
from repositories.task import TaskRepository
from services.task import TaskService

task_repository = TaskRepository()
task_service = TaskService(task_repository)

def get_task_service() -> TaskService:
   return task_service