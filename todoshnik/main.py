from pathlib import Path

from litestar import Litestar
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.static_files import create_static_files_router
from litestar.template.config import TemplateConfig

from todoshnik.pages import index_page

UI_LOCATION = Path('ui')
TEMPLATES_LOCATION = UI_LOCATION / 'src'
STATIC_LOCATION = TEMPLATES_LOCATION / 'assets'

static_files_router = create_static_files_router(
    path='/assets',
    directories=[STATIC_LOCATION],
)

app = Litestar(
    route_handlers=(index_page, static_files_router,),
    template_config=TemplateConfig(
        directory=TEMPLATES_LOCATION,
        engine=JinjaTemplateEngine,
    ),
    openapi_config=None,
)
