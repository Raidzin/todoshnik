from advanced_alchemy.extensions.litestar import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)

session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string='sqlite+aiosqlite:///db.sqlite3',
    before_send_handler='autocommit',
    session_config=session_config,
    create_all=True,
)

sqlalchemy_plugin = SQLAlchemyPlugin(config=sqlalchemy_config)
