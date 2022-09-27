"""Removed resturant_id_fk column from Order table

Revision ID: 0001
Revises: 
Create Date: 2022-09-27 09:57:55.314565

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('order', 'restaurant_id_fk')


def downgrade() -> None:
    pass
