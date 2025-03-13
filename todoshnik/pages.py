from litestar import get
from litestar.plugins.htmx import HTMXTemplate
from litestar.response import Template


@get('')
async def index_page() -> Template:
    return HTMXTemplate(template_name='pages/index.html')