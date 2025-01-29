"""Add 2 columns to student table

Revision ID: a28fcb3299b0
Revises: d9a07b65da02
Create Date: 2025-01-29 15:20:22.224106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a28fcb3299b0'
down_revision: Union[str, None] = 'd9a07b65da02'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('correct_answers', sa.Integer(), nullable=True))
    op.add_column('students', sa.Column('incorrect_answers', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'incorrect_answers')
    op.drop_column('students', 'correct_answers')
    # ### end Alembic commands ###
