import json
import logging
import os.path
from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import path_to_json
from routing.task import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
   print("Сервер запущен")
   logging.basicConfig(level=logging.DEBUG)
   if not os.path.exists(path_to_json):
      with open(path_to_json, "w", encoding='utf-8') as f:
         json.dump(dict(), f)
   yield
   print("Сервер остановлен")

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs", lifespan=lifespan)

app.include_router(task_router)