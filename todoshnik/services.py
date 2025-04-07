from collections.abc import AsyncGenerator

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession

from todoshnik.database.models import Task
from todoshnik.database.repository import TaskRepository


class TaskService(SQLAlchemyAsyncRepositoryService[Task, TaskRepository]):
    repository_type = TaskRepository
    uniquify = True


async def provide_task_service(
    db_session: AsyncSession,
) -> AsyncGenerator[TaskService]:
    async with TaskService.new(session=db_session) as service:
        yield service
