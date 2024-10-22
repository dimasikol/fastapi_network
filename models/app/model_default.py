from datetime import datetime
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase

class BaseModel(AsyncAttrs,DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)


# class MixinDateCreateUpdateModel(AsyncAttrs,DeclarativeBase):
#     id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
#     date_create: Mapped[datetime|None] = mapped_column(default=func.now())
#     date_update: Mapped[datetime|None] = mapped_column(default=func.now(), onupdate=func.now())

