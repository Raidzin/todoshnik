from typing import Annotated
from uuid import UUID

from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.params import Body
from litestar_htmx import HTMXTemplate

from todoshnik.database import dto, models
from todoshnik.database.repository import (
    TaskRepository,
    provide_tag_repository,
    provide_task_repository,
)


class TaskController(Controller):
    path = '/task'
    dependencies = {  # noqa: RUF012
        'task_repository': Provide(provide_task_repository),
        'tag_repository': Provide(provide_tag_repository),
    }

    @get('/create_dialog')
    async def get_task_dialog(
        self, task_repository: TaskRepository
    ) -> HTMXTemplate:
        return HTMXTemplate(
            template_name='components/dialogs/create_task.html',
            re_target='body',
            re_swap='beforeend',
        )

    @post('', dto=dto.TaskDTO)
    async def create_task(
        self,
        task_repository: TaskRepository,
        data: Annotated[
            models.Task,
            Body(media_type=RequestEncodingType.URL_ENCODED),
        ],
    ) -> HTMXTemplate:
        task = await task_repository.add(data=data, auto_commit=True)
        return HTMXTemplate(
            template_name='components/task_item.html',
            context={'task': task},
        )

    @patch('/{task_id:uuid}')
    async def mark_task_is_done(
        self,
        task_id: UUID,
        task_repository: TaskRepository,
    ) -> None:
        task = await task_repository.get(item_id=task_id)
        task.is_done = True
        await task_repository.add(data=task, auto_commit=True)

    @delete('/{task_id:uuid}')
    async def delete_task(
        self,
        task_id: UUID,
        task_repository: TaskRepository,
    ) -> None:
        await task_repository.delete(item_id=task_id)
