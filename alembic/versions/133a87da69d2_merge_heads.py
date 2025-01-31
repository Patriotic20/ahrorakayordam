"""Merge heads

Revision ID: 133a87da69d2
Revises: 5c719f0c795b, d9a07b65da02
Create Date: 2025-01-29 13:50:25.730339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '133a87da69d2'
down_revision: Union[str, None] = ('5c719f0c795b', 'd9a07b65da02')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
