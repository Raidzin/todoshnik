from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from sqlalchemy.ext.asyncio import AsyncSession

from todoshnik.database import models


class TaskRepository(SQLAlchemyAsyncRepository[models.Task]):
    model_type = models.Task


class TagRepository(SQLAlchemyAsyncRepository[models.Tag]):
    model_type = models.Tag


async def provide_task_repository(
    db_session: AsyncSession,
) -> TaskRepository:
    return TaskRepository(session=db_session)


async def provide_tag_repository(
    db_session: AsyncSession,
) -> TagRepository:
    return TagRepository(session=db_session)
