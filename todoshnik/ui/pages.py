from litestar import Controller, get
from litestar.di import Provide
from litestar.plugins.htmx import HTMXTemplate
from litestar.response import Redirect, Template

from todoshnik.database import models
from todoshnik.database.repository import (
    TagRepository,
    TaskRepository,
    provide_tag_repository,
    provide_task_repository,
)
from todoshnik.services import TaskService, provide_task_service


class PagesController(Controller):
    dependencies = {  # noqa: RUF012
        'task_repository': Provide(provide_task_repository),
        'task_service': Provide(provide_task_service),
        'tag_repository': Provide(provide_tag_repository),
    }
    tags = ('Pages',)

    @get('', name='Главная')
    async def index_page(self, task_repository: TaskRepository) -> Redirect:
        return Redirect(path='/tasks')

    @get('/tasks', name='Задачи')
    async def tasks_page(
        self,
        task_service: TaskService,
    ) -> Template:
        tasks = await task_service.list(
            models.Task.is_done == False,  # noqa: E712
        )
        return HTMXTemplate(
            template_name='pages/tasks.html', context={'tasks': tasks}
        )

    @get('/done_tasks', name='Выполнено')
    async def done_tasks_page(
        self, task_repository: TaskRepository
    ) -> Template:
        tasks = await task_repository.list(
            models.Task.is_done == True,  # noqa: E712
        )
        return HTMXTemplate(
            template_name='pages/done_tasks.html', context={'tasks': tasks}
        )

    @get('/tags', name='Отметки')
    async def tags_page(self, tag_repository: TagRepository) -> Template:
        return HTMXTemplate(template_name='pages/tags.html')
