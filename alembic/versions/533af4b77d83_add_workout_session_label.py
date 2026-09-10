"""Add workout session label

Revision ID: 533af4b77d83
Revises: 3de4ebb6d8ed
Create Date: 2026-09-10 23:18:27.680146

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "533af4b77d83"
down_revision: Union[str, Sequence[str], None] = "3de4ebb6d8ed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "workout_sessions",
        sa.Column(
            "label",
            sa.String(length=50),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column(
        "workout_sessions",
        "label",
    )