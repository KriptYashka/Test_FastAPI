import logging
from typing import Optional
from xml.etree.ElementTree import indent

from schemas.task import STask, STaskBody
from config import path_to_json
import json

class JSONReader:
    @classmethod
    def read_json(cls):
        with open(path_to_json, "r", encoding='utf-8') as file:
            json_data = json.load(file)
        return json_data

    @classmethod
    def write_json(cls, json_data):
        with open(path_to_json, "w", encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)


class TaskRepository:
    @classmethod
    def get_next_id(cls) -> int:
        json_data = JSONReader.read_json()
        max_id = 0
        for task_id in json_data:
            max_id = max(max_id, int(task_id))
        return max_id + 1

    @classmethod
    def create_task(cls, task_id: int, task_body: STaskBody) -> STask:
        json_data = JSONReader.read_json()
        json_data[task_id] = task_body.model_dump()
        JSONReader.write_json(json_data)
        task = STask(**task_body.model_dump(), id=task_id)
        return task

    @classmethod
    def get_tasks(cls) -> list[STask]:
        json_data = JSONReader.read_json()
        s_tasks = []
        for task_id in json_data:
            body = json_data[task_id]
            s_task = STask(id=int(task_id), **body)
            s_tasks.append(s_task)
        return s_tasks

    @classmethod
    def get_task_by_id(cls, task_id: str) -> Optional[STask]:
        json_data = JSONReader.read_json()
        if task_id in json_data:
            body = json_data[task_id]
            s_task = STask(id=int(task_id), **body)
            return s_task
        return None

    @classmethod
    def get_tasks_by_category(cls, category: str) -> list[STask]:
        json_data = JSONReader.read_json()
        s_tasks = []
        for task_id in json_data:
            body = json_data[task_id]
            s_task = STask(id=int(task_id), **body)
            if s_task.category == category:
                s_tasks.append(s_task)
        return s_tasks

    @classmethod
    def update_task(cls, task_id: str, task: STaskBody) -> Optional[STask]:
        json_data = JSONReader.read_json()
        if task_id in json_data:
            json_data[task_id] = task.model_dump()
            JSONReader.write_json(json_data)
            s_task = STask(id=int(task_id), **json_data[task_id])
            return s_task
        return None

    @classmethod
    def update_done_task(cls, task_id: str) -> Optional[STask]:
        json_data = JSONReader.read_json()
        if task_id in json_data:
            json_data[task_id]["status"] = "Выполнено"
            JSONReader.write_json(json_data)
            s_task = STask(id=int(task_id), **json_data[task_id])
            return s_task
        return None

    @classmethod
    def delete_task(cls, task_id: str) -> bool:
        json_data = JSONReader.read_json()
        if task_id in json_data:
            del json_data[task_id]
            JSONReader.write_json(json_data)
            return True
        return False
