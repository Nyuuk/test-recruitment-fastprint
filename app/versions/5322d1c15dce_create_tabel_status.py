"""Create Tabel Status

Revision ID: 5322d1c15dce
Revises: 9bb4c0aff0fa
Create Date: 2023-10-04 11:53:49.176457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5322d1c15dce'
down_revision: Union[str, None] = '9bb4c0aff0fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'status',
        sa.Column('id_status', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nama_status', sa.String(50)),
    )


def downgrade() -> None:
    op.drop_table('status')
