import logging
from typing import Optional
from xml.etree.ElementTree import indent

from schemas.task import STask, STaskBody
from config import path_to_json
import json


class TaskRepository:
    @classmethod
    def get_next_id(cls) -> int:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        max_id = 0
        for task_id in json_data:
            max_id = max(max_id, int(task_id))
        return max_id + 1


    @classmethod
    def create_task(cls, task_id: int, task_body: STaskBody) -> STask:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        json_data[task_id] = task_body.model_dump()
        with open(path_to_json, "w", encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
        task = STask(**task_body.model_dump(), id=task_id)
        return task

    @classmethod
    def get_tasks(cls) -> list[STask]:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        s_tasks = []
        for task_id in json_data:
            body = json_data[task_id]
            s_task = STask(id=int(task_id), **body)
            s_tasks.append(s_task)
        return s_tasks

    @classmethod
    def get_task(cls, task_id: str) -> Optional[STask]:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        if task_id in json_data:
            s_task = STask(id=int(task_id), **json_data[task_id])
            return s_task
        return None

    @classmethod
    def update_task(cls, task_id: str, task: STaskBody) -> Optional[STask]:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        if task_id in json_data:
            json_data[task_id] = task.model_dump()
            with open(path_to_json, "w", encoding='utf-8') as file:
                json.dump(json_data, file, ensure_ascii=False, indent=4)
            s_task = STask(id=int(task_id), **json_data[task_id])
            return s_task
        return None

    @classmethod
    def delete_task(cls, task_id: str) -> dict:
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        response = {"status": "OK"}
        if task_id in json_data:
            del json_data[task_id]
            with open(path_to_json, "w", encoding='utf-8') as file:
                json.dump(json_data, file, ensure_ascii=False, indent=4)
        else:
            response["status"] = f"ID: {task_id} not exists"
        return response
