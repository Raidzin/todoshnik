from advanced_alchemy.extensions.litestar import (
    SQLAlchemyDTO,
    SQLAlchemyDTOConfig,
)

from todoshnik.database import models


class TaskDTO(SQLAlchemyDTO[models.Task]):
    config = SQLAlchemyDTOConfig(exclude={'id', 'tags'})


class TagDTO(SQLAlchemyDTO[models.Tag]):
    config = SQLAlchemyDTOConfig(exclude={'id', 'tasks'})
