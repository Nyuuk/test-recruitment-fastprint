"""Create Tabel Products

Revision ID: 154eb9c3cd92
Revises: 5322d1c15dce
Create Date: 2023-10-04 12:08:14.879339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '154eb9c3cd92'
down_revision: Union[str, None] = '5322d1c15dce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
            'products',
            sa.Column('id_produk', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('nama_produk', sa.String(255)),
            sa.Column('harga', sa.Integer),

            sa.Column('kategori_id', sa.Integer, sa.ForeignKey('categories.id_kategori')),
            sa.Column('status_id', sa.Integer, sa.ForeignKey('status.id_status')),

            # sa.ForeignKeyConstraint(['kategori_id'], ['categories.id_kategori']),
            # sa.ForeignKeyConstraint(['status_id'], ['status.id_status']),
        )


def downgrade() -> None:
    op.drop_table('products')