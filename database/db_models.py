from database.db_config import DatabaseConfig
from database.db_creator import PostgresHandler

db_passcode = DatabaseConfig.password.replace("%", "%%")
handler = PostgresHandler(
    DatabaseConfig.host,
    DatabaseConfig.username,
    DatabaseConfig.password,
    DatabaseConfig.port,
    DatabaseConfig.database_name,
    DatabaseConfig.pool_size,
)


def create_model():
    handler.initialize_db()

    handler.Base.metadata.create_all(bind=handler.engine)
