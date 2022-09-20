from sqlalchemy import create_engine
from sqlalchemy.engine import reflection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database
from database.db_config import DatabaseConfig


class PostgresHandler:
    """
    MySQL handler for db query
    """

    def __init__(
            self,
            host,
            username,
            password,
            port=DatabaseConfig.port,
            database_name="",
            pool_size=DatabaseConfig.pool_size,
    ):
        self.host = host
        self.__username = username
        self.__password = password
        self.port = int(port)
        self.database_name = database_name
        self.pool_size = int(pool_size)
        self.url = None
        self._validate_credentials()
        self._create_engine()

    def _validate_credentials(self):
        if self.host is None:
            raise ValueError("No host specified for postgres")
        if self.__username is None:
            raise ValueError("No user specified for postgres")
        if self.__password is None:
            raise ValueError("No password specified for postgres")
        if self.database_name is None or self.database_name == "":
            raise ValueError("No db specified for postgres")

    def _create_engine(self):

        # self.engine = create_engine(
        #     self.url, pool_size=self.pool_size, pool_pre_ping=True, pool_recycle=300, echo=False,
        #     isolation_level="READ UNCOMMITTED")
        self.engine = create_engine(f'postgresql://{self.__username}:{self.__password}@{self.host}:{self.port}/'
                                    f'{self.database_name}')
        self.db_session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )
        self.Base = declarative_base(bind=self.engine)
        self.Base.query = self.db_session.query_property()

    def initialize_db(self):
        """
        Create db if not exists
        """
        if not database_exists(self.engine.url):
            # pylint: disable=E1101
            # Note: Disabled no-member as engine is a instance of sqlalchemy
            create_database(self.engine.url)
        else:
            # Connect the database if exists.
            self.engine.connect()


def table_has_column(table, column):
    handler = PostgresHandler(
        DatabaseConfig.host,
        DatabaseConfig.username,
        DatabaseConfig.password,
        DatabaseConfig.port,
        DatabaseConfig.database_name,
        DatabaseConfig.pool_size,
    )

    insp = reflection.Inspector.from_engine(handler.engine)
    has_column = False
    for col in insp.get_columns(table):
        if column not in col['name']:
            continue
        has_column = True
    return has_column


def db_has_table(table):
    handler = PostgresHandler(
        DatabaseConfig.host,
        DatabaseConfig.username,
        DatabaseConfig.password,
        DatabaseConfig.port,
        DatabaseConfig.database_name,
        DatabaseConfig.pool_size,
    )

    insp = reflection.Inspector.from_engine(handler.engine)
    has_table = False
    for tbl in insp.get_table_names():
        if table not in tbl:
            continue
        has_table = True
    return has_table
