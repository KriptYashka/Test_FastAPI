from typing import List, Optional

import typer
from pydantic_core._pydantic_core import ValidationError

from depends import get_task_service
from schemas.task import STask, STaskBody

app = typer.Typer()

@app.command(
   name="all"
)
def get_all_tasks():
   tasks = get_task_service().get_tasks()
   print(tasks)

@app.command(
   name="get"
)
def get_task(task_search: str):
   task = get_task_service().get_task(task_search)
   print(task)


@app.command(
   name="create"
)
def create_task(
         name: str,
         description: str,
         category: str,
         due_date: str,
         priority: str,
         status: str
):

   try:
      task_body = STaskBody(
         name = name,
         description = description,
         category = category,
         due_date = due_date,
         priority = priority,
         status = status)
      STaskBody.model_validate(task_body)
   except ValidationError as e:
      print(e)
   else:
      task = get_task_service().create_task(task_body)
      print(task)
# @router.post(
#    "/",
#    responses={400: {"description": "Bad request"}},
#    response_model=STask,
#    description="Создание задачи",
# )
# async def get_all_tasks(
#         _task: STaskBody,
#         task_service: TaskService = Depends(get_task_service),
# ) -> STask:
#    logging.debug("Создание задачи")
#    task = task_service.create_task(_task)
#    logging.debug("Задача создана")
#    return task
#
# @router.get(
#    "/{task_id}/",
#    responses={400: {"description": "Bad request"}},
#    response_model=Optional[STask],
#    description="Получение задачи",
# )
# async def get_task(
#         task_id: str,
#         task_service: TaskService = Depends(get_task_service),
# ) -> Optional[STask]:
#    task = task_service.get_task(task_id)
#    return task
#
# @router.put(
#    "/{task_id}/",
#    responses={400: {"description": "Bad request"}},
#    response_model=Optional[STask],
#    description="Обновление задачи",
# )
# async def update_task(
#         task_id: str,
#         task_body: STaskBody,
#         task_service: TaskService = Depends(get_task_service),
# ) -> Optional[STask]:
#    task = task_service.update_task(task_id, task_body)
#    return task
#
# @router.delete(
#    "/{task_id}/",
#    responses={400: {"description": "Bad request"}},
#    response_model=dict,
#    description="Удаление задачи",
# )
# async def delete_task(
#         task_id: str,
#         task_service: TaskService = Depends(get_task_service),
# ) -> dict:
#    task = task_service.delete_task(task_id)
#    return task