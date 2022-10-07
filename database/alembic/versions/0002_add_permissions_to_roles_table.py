"""add permissions to roles table

Revision ID: 0002
Revises: 0001
Create Date: 2022-10-07 11:33:49.852369

"""
from alembic import op
import sqlalchemy as sa
from common import role_constant
import json


# revision identifiers, used by Alembic.
revision = '0002'
down_revision = '0001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        f"INSERT INTO roles (role_name, role_display_name, resources) VALUES ('restaurant_owner', 'Restaurant Owner', "
        f"'{json.dumps(role_constant.Roles.RESTAURANT_PERMISSION)}')")
    op.execute(
        f"INSERT INTO roles (role_name, role_display_name, resources) VALUES ('user', 'User', "
        f"'{json.dumps(role_constant.Roles.USER_PERMISSION)}')")
    op.execute(
        f"INSERT INTO roles (role_name, role_display_name, resources) VALUES ('delivery_agent', 'Delivery Agent', "
        f"'{json.dumps(role_constant.Roles.DELIVERY_AGENT_PERMISSION)}')")


def downgrade() -> None:
    pass
