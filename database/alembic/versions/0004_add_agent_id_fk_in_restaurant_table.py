"""add agent_id_fk in restaurant table

Revision ID: 0004
Revises: 0003
Create Date: 2022-10-03 11:55:39.980754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0004'
down_revision = '0003'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('restaurant', sa.Column('agent_id_fk', sa.Integer))


def downgrade() -> None:
    op.drop_column('restaurant', sa.Column('agent_id_fk', sa.Integer))
