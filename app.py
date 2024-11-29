from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from routing.task import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
   await create_tables()
   print("База готова")
   yield
   # await delete_tables()
   # print("База очищена")

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs", lifespan=lifespan)

app.include_router(task_router)