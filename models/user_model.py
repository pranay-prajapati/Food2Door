from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    LargeBinary,
    JSON,
    Enum,

)
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import func, expression
# from database.db_creator import PostgresHandler
from database.db_models import handler


class User(handler.Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    contact_number = Column(String(10), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    address = Column(String(256))
    city = Column(String(64))
    state = Column(String(64))
    zip_code = Column(String(6))
    password_hash = Column(LargeBinary(64))
    is_owner = Column(Boolean, server_default=expression.false())
    is_delivery_agent = Column(Boolean, server_default=expression.false())
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP)

    def __repr__(self):
        return '<User %r>' % self.name
