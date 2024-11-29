from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Model(DeclarativeBase):
   pass

class TaskOrm(Model):
   __tablename__ = "tasks"
   id: Mapped[int] = mapped_column(primary_key=True)
   name: Mapped[str]
   description: Mapped[str | None]
   category: Mapped[str]
   due_date: Mapped[datetime]
   priority: Mapped[str]
   status: Mapped[str]
