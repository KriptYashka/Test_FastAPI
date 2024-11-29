from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class STask(BaseModel):
   id: int
   name: str
   description: Optional[str]
   category: str
   due_date: datetime
   priority: str
   status: str