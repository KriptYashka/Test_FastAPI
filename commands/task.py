from datetime import datetime
from typing import List, Optional

import typer

from depends import get_task_service
from schemas.task import STask, STaskBody

app = typer.Typer()

@app.command(
    name="all"
)
def get_all_tasks():
    """
    Выводит все задачи.
    """
    tasks = get_task_service().get_tasks()
    for task in tasks:
        print(task)

@app.command(
    name="get"
)
def get_task(
        id: Optional[int] = None,
        category: Optional[str] = None,
):
    """
    Выводит задачи по одному из заданных опций:
    --id
    --category
    """
    if id is not None:
        task = get_task_service().get_task_by_id(str(id))
        print(task)
    elif category is not None:
        tasks = get_task_service().get_task_by_category(category)
        for task in tasks:
            print(task)
    else:
        print("Enter one of both options. --help for information.")


@app.command(
    name="add"
)
def create_task(
        name:        str,
        description: str,
        category:    str,
        due_date:    datetime,
        priority:    str,
        status:      str
):
    """
    Создаёт задачу. Параметры можно посмотреть по команде `python app.py add --help`.
    """
    task_body = STaskBody(
        name = name,
        description = description,
        category = category,
        due_date = due_date,
        priority = priority,
        status = status)
    task = get_task_service().create_task(task_body)
    print(task)


@app.command(
    name="update"
)
def update_task(
        task_id: int,
        name:        Optional[str] = None,
        description: Optional[str] = None,
        category:    Optional[str] = None,
        due_date:    Optional[datetime] = None,
        priority:    Optional[str] = None,
        status:      Optional[str] = None
):
    """
    Обновляет параметры задачи. Опции можно посмотреть по команде `python app.py update --help`.
    """
    task = get_task_service().get_task_by_id(str(task_id))
    task_body = STaskBody(
        name= name or task.name,
        description = description or task.description,
        category = category or task.category,
        due_date = due_date or task.due_date,
        priority = priority or task.priority,
        status = status or task.status
    )
    updated_task = get_task_service().update_task(str(task_id), task_body)
    print(updated_task)

@app.command(
    name="done"
)
def update_done_task(
        task_id: int
):
    """
    Обновляет статус с tack_id задачи на "Выполнено".
    """
    result = get_task_service().update_done_task(str(task_id))
    print(result)

@app.command(
    name="rm"
)
def delete_task(
        task_id: int
):
    """
    Удаляет задачу с task_id.
    """
    result = get_task_service().delete_task(str(task_id))
    print(result)
