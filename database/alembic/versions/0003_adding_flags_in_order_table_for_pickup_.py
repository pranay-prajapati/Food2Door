"""adding flags in order table for pickup and accept

Revision ID: 0003
Revises: 0002
Create Date: 2022-10-17 17:55:22.602413

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression

# revision identifiers, used by Alembic.
revision = '0003'
down_revision = '0002'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('order', sa.Column('is_picked', sa.BOOLEAN, server_default=expression.false()))
    op.add_column('order', sa.Column('is_accepted', sa.BOOLEAN, server_default=expression.false()))


def downgrade() -> None:
    op.drop_column('order', sa.Column('is_picked', sa.BOOLEAN, server_default=expression.false()))
    op.drop_column('order', sa.Column('is_accepted', sa.BOOLEAN, server_default=expression.false()))