from pathlib import Path

from litestar import Litestar
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.static_files import create_static_files_router
from litestar.template.config import TemplateConfig

from todoshnik.database.plugin import sqlalchemy_plugin
from todoshnik.templates import template_filters, templates_globals
from todoshnik.ui import components, pages

UI_LOCATION = Path('ui')
TEMPLATES_LOCATION = UI_LOCATION / 'src'
PUBLIC_LOCATION = UI_LOCATION / 'public'
ASSETS_LOCATION = TEMPLATES_LOCATION / 'assets'

public_router = create_static_files_router(
    path='/',
    directories=[PUBLIC_LOCATION],
)
assets_router = create_static_files_router(
    path='/assets',
    directories=[ASSETS_LOCATION],
)

template_engine = JinjaTemplateEngine(TEMPLATES_LOCATION)
template_engine.engine.globals.update(templates_globals)
template_engine.engine.filters.update(template_filters)

app = Litestar(
    route_handlers=(
        pages.PagesController,
        components.TaskController,
        public_router,
        assets_router,
    ),
    template_config=TemplateConfig(
        engine=template_engine,
    ),
    plugins=(sqlalchemy_plugin,),
    openapi_config=None,
)
