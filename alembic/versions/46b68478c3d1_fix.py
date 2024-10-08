"""fix

Revision ID: 46b68478c3d1
Revises: 6a4b0354b40c
Create Date: 2024-08-19 00:06:45.411886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46b68478c3d1'
down_revision: Union[str, None] = '6a4b0354b40c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('beak', sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('breast', sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('leg', sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.alter_column('training', 'name_training',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('training', 'name_training',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('leg', 'date')
    op.drop_column('breast', 'date')
    op.drop_column('beak', 'date')
    # ### end Alembic commands ###
