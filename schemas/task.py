import json
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class STaskBody(BaseModel):
   name: str
   description: Optional[str]
   category: str
   due_date: datetime
   priority: str
   status: str

class STask(STaskBody):
   id: int

   def __str__(self):
      data = self.model_dump()
      return json.dumps(data, ensure_ascii=False, indent=4, default=str)
