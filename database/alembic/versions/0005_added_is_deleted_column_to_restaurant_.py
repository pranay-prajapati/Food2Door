"""Added is_deleted column to restaurant table

Revision ID: 0005
Revises: 0004
Create Date: 2022-11-01 16:58:11.913074

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression

# revision identifiers, used by Alembic.
revision = '0005'
down_revision = '0004'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('restaurant', sa.Column('is_deleted', sa.BOOLEAN, server_default=expression.false()))


def downgrade() -> None:
    op.drop_column('restaurant', sa.Column('is_deleted', sa.BOOLEAN, server_default=expression.false()))
