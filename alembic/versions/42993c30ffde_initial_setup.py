"""create product and shop tables

Revision ID: 42993c30ffde
Revises: 
Create Date: 2022-02-20 11:33:46.206231

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from app.models import Unit
from sqlalchemy_utils import ChoiceType

# revision identifiers, used by Alembic.
revision = "42993c30ffde"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "shops",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(50), nullable=False),
    )
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(50), nullable=False, unique=True),
        sa.Column("description", sa.String(200), nullable=True),
        sa.Column("updated_at", sa.DateTime, default=datetime.now()),
    )

    op.create_table(
        "quantities",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "unit",
            ChoiceType(Unit, impl=sa.String(50)),
            nullable=False,
        ),
        sa.Column("value", sa.Float, nullable=False),
    )

    op.create_table(
        "product_shops",
        sa.Column(
            "product_id", sa.Integer, sa.ForeignKey("products.id"), onupdate="CASCADE"
        ),
        sa.Column("shop_id", sa.Integer, sa.ForeignKey("shops.id"), onupdate="CASCADE"),
        sa.Column(
            "quantity_id",
            sa.Integer,
            sa.ForeignKey("quantities.id"),
            onupdate="CASCADE",
        ),
        sa.Column("price", sa.Float, nullable=False),
        sa.PrimaryKeyConstraint("product_id", "shop_id", "quantity_id"),
    )


def downgrade():
    op.drop_table("product_shops")
    op.drop_table("quantities")
    op.drop_table("products")
    op.drop_table("shops")
