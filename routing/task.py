import logging
from typing import List, Optional

from fastapi import APIRouter, Depends2222

from depends import get_task_service
from schemas.task import STask, STaskBody
from services.task import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
   "/",
   responses={400: {"description": "Bad request"}},
   response_model=List[STask],
   description="Получение всех задач",
)
async def get_all_books(
       task_service: TaskService = Depends(get_task_service),
) -> List[STask]:
   books = task_service.get_tasks()
   return books


@router.post(
   "/",
   responses={400: {"description": "Bad request"}},
   response_model=STask,
   description="Создание задачи",
)
async def get_all_tasks(
        _task: STaskBody,
        task_service: TaskService = Depends(get_task_service),
) -> STask:
   logging.debug("Создание задачи")
   task = task_service.create_task(_task)
   logging.debug("Задача создана")
   return task

@router.get(
   "/{task_id}/",
   responses={400: {"description": "Bad request"}},
   response_model=Optional[STask],
   description="Получение задачи",
)
async def get_task(
        task_id: str,
        task_service: TaskService = Depends(get_task_service),
) -> Optional[STask]:
   task = task_service.get_task(task_id)
   return task

@router.put(
   "/{task_id}/",
   responses={400: {"description": "Bad request"}},
   response_model=Optional[STask],
   description="Обновление задачи",
)
async def update_task(
        task_id: str,
        task_body: STaskBody,
        task_service: TaskService = Depends(get_task_service),
) -> Optional[STask]:
   task = task_service.update_task(task_id, task_body)
   return task

@router.delete(
   "/{task_id}/",
   responses={400: {"description": "Bad request"}},
   response_model=dict,
   description="Удаление задачи",
)
async def delete_task(
        task_id: str,
        task_service: TaskService = Depends(get_task_service),
) -> dict:
   task = task_service.delete_task(task_id)
   return task