from datetime import UTC, datetime
from uuid import UUID

from litestar.contrib.pydantic import PydanticDTO
from litestar.dto import DTOConfig
from pydantic import BaseModel as _BaseModel
from pydantic import ConfigDict, Field


class BaseModel(_BaseModel):
    model_config = ConfigDict(from_attributes=True)


class Task(BaseModel):
    id: UUID | None = None
    name: str
    description: str | None
    is_done: bool = False
    creation_date: datetime | None = Field(
        default_factory=lambda: datetime.now(tz=UTC)
    )


class TaskDTO(PydanticDTO[Task]):
    config = DTOConfig(exclude={'id'})
