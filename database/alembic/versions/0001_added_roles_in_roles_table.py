"""Added roles in Roles table

Revision ID: 0001
Revises: 
Create Date: 2022-10-07 14:45:00.982300

"""
from alembic import op
import sqlalchemy as sa
import json
from common import role_constant


# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
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
