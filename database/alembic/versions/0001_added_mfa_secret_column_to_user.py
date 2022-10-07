"""Added mfa_secret column to User

Revision ID: 0001
Revises:
Create Date: 2022-10-04 15:44:05.353987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.add_column('user', sa.Column('mfa_secret', sa.String))
    pass

def downgrade() -> None:
    # op.drop_column('user', sa.Column('mfa_secret', sa.String))
    pass
