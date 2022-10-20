"""adding flag is_ordered in Order table

Revision ID: 0004
Revises: 0003
Create Date: 2022-10-19 12:33:42.297464

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import expression

# revision identifiers, used by Alembic.
revision = '0004'
down_revision = '0003'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.add_column('order', sa.Column('is_ordered', sa.BOOLEAN, server_default=expression.false()))
    # op.add_column('order', sa.Column('price', sa.Float))
    # op.add_column('cart',sa.Column('user_id_fk', sa.Integer))
    pass

def downgrade() -> None:
    # op.drop_column('order', sa.Column('is_ordered', sa.BOOLEAN, server_default=expression.false()))
    # op.drop_column('order', sa.Column('price', sa.Float))
    pass
