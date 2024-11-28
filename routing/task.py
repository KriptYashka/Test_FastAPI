from typing import List

from fastapi import APIRouter, Depends

from depends import get_task_service
from schemas.task import Task
from services.task import TaskService

router = APIRouter(prefix="/books", tags=["books"])


@router.get(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=List[Task],
   description="Получение всех задач",
)
async def get_all_books(
       task_service: TaskService = Depends(get_task_service),
) -> List[Task]:
   books = task_service.get_books()
   return books


@router.post(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=Task,
   description="Создание задачи",
)
async def get_all_books(
       task_service: TaskService = Depends(get_task_service),
) -> Task:
   task = task_service.create_book()
   return task