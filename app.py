from fastapi import FastAPI

from routing.task import router as task_router

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.include_router(task_router)
