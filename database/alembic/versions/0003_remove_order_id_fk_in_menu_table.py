"""remove order_id_fk in menu table

Revision ID: 0003
Revises: 0002
Create Date: 2022-09-27 18:06:32.034490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0003'
down_revision = '0002'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('menu', 'order_id_fk')


def downgrade() -> None:
    pass
