from xml.etree.ElementTree import indent

from schemas.task import STask
from config import path_to_json
import json


class TaskRepository:
    @classmethod
    def create_task(cls, task: STask) -> STask:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        json_data["tasks"].append(task.model_dump())
        with open(path_to_json, "w", encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
        return task

    @classmethod
    def get_tasks(cls) -> list[STask]:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        s_tasks = []
        for task in json_data["tasks"]:
            s_task = STask(**task)
            s_tasks.append(s_task)
        return s_tasks

    @classmethod
    def get_task(cls, obj_id: int):
        pass

    @classmethod
    def update_task(cls, task: STask) -> STask:
        pass