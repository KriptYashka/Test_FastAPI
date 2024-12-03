from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class STaskBody(BaseModel):
   name: str
   description: Optional[str]
   category: str
   due_date: str
   priority: str
   status: str

class STask(STaskBody):
   id: int
