"""create products table

Revision ID: b8eb5e102b12
Revises: 
Create Date: 2022-02-18 14:53:21.360477

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b8eb5e102b12"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("last_modified", sa.DateTime, default=datetime.now()),
    )


def downgrade():
    op.drop_table("products")
