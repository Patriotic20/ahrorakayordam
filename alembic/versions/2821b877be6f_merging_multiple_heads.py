"""Merging multiple heads

Revision ID: 2821b877be6f
Revises: c59e8d077b9a, e16ab9b56a1f
Create Date: 2025-01-31 14:29:35.774403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2821b877be6f'
down_revision: Union[str, None] = ('c59e8d077b9a', 'e16ab9b56a1f')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
