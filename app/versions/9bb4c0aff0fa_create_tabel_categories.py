"""Create Tabel Categories

Revision ID: 9bb4c0aff0fa
Revises:
Create Date: 2023-10-04 11:53:43.401279
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bb4c0aff0fa'
down_revision: Union[str, None] = ''
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'categories',
        sa.Column('id_kategori', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nama_kategori', sa.String(50)),
    )


def downgrade() -> None:
    op.drop_table('categories')
