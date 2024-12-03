from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class STaskId(BaseModel):
   id: int

class STaskBody(BaseModel):
   name: str
   description: Optional[str]
   category: str
   due_date: datetime
   priority: str
   status: str

class STask(STaskBody, STaskId):
   pass
