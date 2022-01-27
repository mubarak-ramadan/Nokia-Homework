"""create meal table

Revision ID: 8c034d4099d0
Revises: 4c08e8fc949a
Create Date: 2022-01-16 13:24:38.372729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c034d4099d0'
down_revision = '4c08e8fc949a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'meals',
        sa.Column("id", sa.Integer, primary_key=True, unique=True),
        sa.Column("name", sa.String, index=True, nullable=False, unique=True),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("ingredients", sa.Text, index=True),
        sa.Column("spicy",sa.Boolean, index=True, default=False),
        sa.Column("vegan",sa.Boolean, index=True, default=False),
        sa.Column("gluten" ,sa.Boolean, index=True, default=False),
        sa.Column("description" ,sa.Text, index=True),
        sa.Column("kcal" ,sa.Float),
        sa.Column("picture", sa.String)
    )


def downgrade():
    pass
