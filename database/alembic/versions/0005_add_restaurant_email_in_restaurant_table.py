"""add restaurant_email in restaurant table

Revision ID: 0005
Revises: 0004
Create Date: 2022-10-03 15:13:46.335959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0005'
down_revision = '0004'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('restaurant', sa.Column('restaurant_email', sa.Integer))


def downgrade() -> None:
    op.drop_column('restaurant', sa.Column('restaurant_email', sa.Integer))
