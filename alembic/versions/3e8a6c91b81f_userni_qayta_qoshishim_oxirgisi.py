"""userni qayta qoshishim oxirgisi

Revision ID: 3e8a6c91b81f
Revises: 12faa4a59baf, a28fcb3299b0
Create Date: 2025-01-29 16:13:20.464310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e8a6c91b81f'
down_revision: Union[str, None] = ('12faa4a59baf', 'a28fcb3299b0')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
