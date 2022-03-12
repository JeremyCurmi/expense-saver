"""create product and shop tables

Revision ID: 42993c30ffde
Revises: 
Create Date: 2022-02-20 11:33:46.206231

"""
from datetime import datetime

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

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
        sa.Column("updated_at", sa.DateTime, default=datetime.utcnow()),
    )

    op.create_table(
        "quantities",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "unit",
            sa.String(50),
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

    op.create_table(
        "categories",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column(
            "name",
            sa.String(50),
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
    op.create_table(
        "accounts",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_accounts_id"), "accounts", ["id"], unique=False)
    op.create_index(op.f("ix_accounts_name"), "accounts", ["name"], unique=False)

    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=True),
        sa.Column("phone_number", sa.String(length=13), nullable=True),
        sa.Column("email", sa.String(length=100), nullable=False, unique=True),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("account_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.ForeignKeyConstraint(["account_id"], ["accounts.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_index(
        op.f("ix_users_full_name"), "users", ["full_name"], unique=False
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)
    op.create_index(
        op.f("ix_users_phone_number"), "users", ["phone_number"], unique=True
    )


    op.create_table(
        "roles",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_roles_id"), "roles", ["id"], unique=False)
    op.create_index(op.f("ix_roles_name"), "roles", ["name"], unique=False)

    op.create_table(
        "user_roles",
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("role_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(["role_id"], ["roles.id"], ),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ),
        sa.PrimaryKeyConstraint("user_id", "role_id"),
        sa.UniqueConstraint("user_id", "role_id", name="unique_user_role"),
    )

def downgrade():
    op.drop_table("user_roles")
    op.drop_table("roles")
    op.drop_table("users")
    op.drop_table("accounts")
    op.drop_table("product_categories")
    op.drop_table("categories")
    op.drop_table("product_shops")
    op.drop_table("quantities")
    op.drop_table("products")
    op.drop_table("shops")
