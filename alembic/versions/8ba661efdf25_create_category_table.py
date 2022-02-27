"""create category table

Revision ID: 8ba661efdf25
Revises: 42993c30ffde
Create Date: 2022-02-21 06:57:19.434131

"""
import sqlalchemy as sa
from alembic import op
from app.models import CategoryType
from sqlalchemy_utils import ChoiceType

# revision identifiers, used by Alembic.
revision = "8ba661efdf25"
down_revision = "42993c30ffde"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "name",
            ChoiceType(CategoryType, impl=sa.String(50)),
            nullable=False,
            unique=True,
        ),
    )

    op.create_table(
        "product_categories",
        sa.Column(
            "product_id", sa.Integer, sa.ForeignKey("products.id"), onupdate="CASCADE"
        ),
        sa.Column(
            "category_id",
            sa.Integer,
            sa.ForeignKey("categories.id"),
            onupdate="CASCADE",
        ),
        sa.PrimaryKeyConstraint("product_id", "category_id"),
    )


def downgrade():
    op.drop_table("product_categories")
    op.drop_table("categories")
