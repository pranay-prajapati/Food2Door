"""Added order_id_fk in menu table

Revision ID: 0002
Revises: 0001
Create Date: 2022-09-27 18:02:07.421494

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('menu', sa.Column('order_id_fk', sa.Integer))


def downgrade() -> None:
    op.drop_column('menu', sa.Column('order_id_fk', sa.Integer))
