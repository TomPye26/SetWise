"""make workout session routine optional

Revision ID: 5cc23cdf712c
Revises: e4109700fd90
Create Date: 2026-09-06 22:58:35.046891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5cc23cdf712c'
down_revision: Union[str, Sequence[str], None] = 'e4109700fd90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("workout_sessions") as batch_op:
        batch_op.alter_column(
            "workout_id",
            existing_type=sa.INTEGER(),
            nullable=True,
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("workout_sessions") as batch_op:
        batch_op.alter_column(
            "workout_id",
            existing_type=sa.INTEGER(),
            nullable=False,
        )