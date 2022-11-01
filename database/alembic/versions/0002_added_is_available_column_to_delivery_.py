"""Added is_available column to delivery agent table

Revision ID: 0002
Revises: 0001
Create Date: 2022-10-17 17:33:06.296368

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression

# revision identifiers, used by Alembic.
revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('delivery_agent', sa.Column('is_available', sa.BOOLEAN, server_default=expression.true()))


def downgrade():
    op.drop_column('delivery_agent', sa.Column('is_available', sa.BOOLEAN, server_default=expression.true()))
