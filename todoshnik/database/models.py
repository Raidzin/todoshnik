from datetime import UTC, datetime

from advanced_alchemy.base import UUIDBase
from advanced_alchemy.types import DateTimeUTC
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

task_tag_association_table = Table(
    'task_tag_association',
    UUIDBase.metadata,
    Column('task_id', ForeignKey('task.id'), primary_key=True),
    Column('tag_id', ForeignKey('tag.id'), primary_key=True),
)


class Task(UUIDBase):
    __tablename__ = 'task'

    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    is_done: Mapped[bool] = mapped_column(default=False)
    creation_date: Mapped[datetime] = mapped_column(
        DateTimeUTC(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    tags: Mapped[list['Tag']] = relationship(
        secondary=task_tag_association_table,
        back_populates='tasks',
        lazy='joined',
    )


class Tag(UUIDBase):
    __tablename__ = 'tag'

    name: Mapped[str]

    tasks: Mapped[list[Task]] = relationship(
        secondary=task_tag_association_table,
        back_populates='tags',
    )
