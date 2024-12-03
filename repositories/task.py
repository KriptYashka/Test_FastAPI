import logging
from xml.etree.ElementTree import indent

from schemas.task import STask, STaskBody
from config import path_to_json
import json


class TaskRepository:
    @classmethod
    def create_task(cls, task_id: int, task_body: STaskBody) -> STask:
        logging.debug("Старт функции")
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        json_data["tasks"].append({task_id: task_body.model_dump()})
        with open(path_to_json, "w", encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
        task = STask(**task_body.model_dump(), id=task_id)
        logging.debug("Задача создана")
        return task

    @classmethod
    def get_tasks(cls) -> list[STask]:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        s_tasks = []
        for task_id in json_data["tasks"]:
            body = json_data["tasks"][task_id]
            s_task = STask(id=int(task_id), **body)
            s_tasks.append(s_task)
        return s_tasks

    @classmethod
    def get_task(cls, obj_id: int):
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)

    @classmethod
    def update_task(cls, task: STask) -> STask:
        pass

    @classmethod
    def get_next_id(cls) -> int:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        max_id = 0
        for task_id in json_data["tasks"]:
            max_id = max(max_id, task_id)
        return max_id + 1