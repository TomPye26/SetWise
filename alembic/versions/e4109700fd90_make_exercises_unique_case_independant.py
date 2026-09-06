"""make exercises unique case independant

Revision ID: e4109700fd90
Revises: 1a8cf9bb15dc
Create Date: 2026-09-06 21:25:39.702553

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "e4109700fd90"
down_revision: Union[str, Sequence[str], None] = "1a8cf9bb15dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute(
        sa.text(
            "CREATE UNIQUE INDEX uq_exercise_name_lower "
            "ON exercises (LOWER(name))"
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
        sa.text(
            "DROP INDEX uq_exercise_name_lower"
        )
    )
