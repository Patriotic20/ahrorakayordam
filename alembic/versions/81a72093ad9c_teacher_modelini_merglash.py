"""Teacher Modelini Merglash 

Revision ID: 81a72093ad9c
Revises: 0a3bb17f8682, a715a910a5fa
Create Date: 2025-01-31 16:03:16.057207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81a72093ad9c'
down_revision: Union[str, None] = ('0a3bb17f8682', 'a715a910a5fa')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
