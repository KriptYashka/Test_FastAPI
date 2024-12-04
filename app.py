import json
import logging
import os.path

import typer

from config import path_to_json
from depends import get_task_service

from commands.task import app



if __name__ == '__main__':
   print("Сервер запущен")
   logging.basicConfig(level=logging.DEBUG)
   if not os.path.exists(path_to_json):
      with open(path_to_json, "w", encoding='utf-8') as f:
         json.dump(dict(), f)
   app()
   print("Сервер остановлен")