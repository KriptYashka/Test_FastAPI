from datetime import datetime
from pydantic import BaseModel


class Task(BaseModel):
   id: str
   title: str
   description: str
   category: str
   due_date: datetime
   priority: str
   status: str