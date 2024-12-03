from typing import List

from fastapi import APIRouter, Depends

from depends import get_task_service
from schemas.task import STask
from services.task import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=List[STask],
   description="Получение всех задач",
)
async def get_all_books(
       task_service: TaskService = Depends(get_task_service),
) -> List[STask]:
   books = await task_service.get_tasks()
   return books


@router.post(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=STask,
   description="Создание задачи",
)
async def get_all_tasks(
        _task: STask,
        task_service: TaskService = Depends(get_task_service),
) -> STask:
   task = await task_service.create_task(_task)
   return task

@router.put(
   "",
   responses={400: {"description": "Bad request"}},
   response_model=STask,
   description="Редактирование задачи",
)
async def update_task(
        _task: STask,
        task_service: TaskService = Depends(get_task_service),
) -> STask:
   task = await task_service.update_task(_task)
   return task