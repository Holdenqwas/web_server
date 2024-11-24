"""fix

Revision ID: ac0c6019d480
Revises: fe3a4028642b
Create Date: 2024-11-24 16:30:06.785040

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac0c6019d480'
down_revision: Union[str, None] = 'fe3a4028642b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop_list',
    sa.Column('uid', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('array_user_id', sa.ARRAY(sa.BigInteger()), nullable=True),
    sa.Column('items', sa.ARRAY(sa.Text()), nullable=True),
    sa.Column('update_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('train1',
    sa.Column('uid', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('ex1', sa.Float(), nullable=True),
    sa.Column('ex2', sa.Float(), nullable=True),
    sa.Column('ex3', sa.Float(), nullable=True),
    sa.Column('ex4', sa.Float(), nullable=True),
    sa.Column('ex5', sa.Float(), nullable=True),
    sa.Column('ex6', sa.Float(), nullable=True),
    sa.Column('ex7', sa.Float(), nullable=True),
    sa.Column('ex8', sa.Float(), nullable=True),
    sa.Column('ex9', sa.Float(), nullable=True),
    sa.Column('ex10', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('train2',
    sa.Column('uid', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('ex1', sa.Float(), nullable=True),
    sa.Column('ex2', sa.Float(), nullable=True),
    sa.Column('ex3', sa.Float(), nullable=True),
    sa.Column('ex4', sa.Float(), nullable=True),
    sa.Column('ex5', sa.Float(), nullable=True),
    sa.Column('ex6', sa.Float(), nullable=True),
    sa.Column('ex7', sa.Float(), nullable=True),
    sa.Column('ex8', sa.Float(), nullable=True),
    sa.Column('ex9', sa.Float(), nullable=True),
    sa.Column('ex10', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('train3',
    sa.Column('uid', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('ex1', sa.Float(), nullable=True),
    sa.Column('ex2', sa.Float(), nullable=True),
    sa.Column('ex3', sa.Float(), nullable=True),
    sa.Column('ex4', sa.Float(), nullable=True),
    sa.Column('ex5', sa.Float(), nullable=True),
    sa.Column('ex6', sa.Float(), nullable=True),
    sa.Column('ex7', sa.Float(), nullable=True),
    sa.Column('ex8', sa.Float(), nullable=True),
    sa.Column('ex9', sa.Float(), nullable=True),
    sa.Column('ex10', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('train4',
    sa.Column('uid', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('ex1', sa.Float(), nullable=True),
    sa.Column('ex2', sa.Float(), nullable=True),
    sa.Column('ex3', sa.Float(), nullable=True),
    sa.Column('ex4', sa.Float(), nullable=True),
    sa.Column('ex5', sa.Float(), nullable=True),
    sa.Column('ex6', sa.Float(), nullable=True),
    sa.Column('ex7', sa.Float(), nullable=True),
    sa.Column('ex8', sa.Float(), nullable=True),
    sa.Column('ex9', sa.Float(), nullable=True),
    sa.Column('ex10', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('train5',
    sa.Column('uid', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('ex1', sa.Float(), nullable=True),
    sa.Column('ex2', sa.Float(), nullable=True),
    sa.Column('ex3', sa.Float(), nullable=True),
    sa.Column('ex4', sa.Float(), nullable=True),
    sa.Column('ex5', sa.Float(), nullable=True),
    sa.Column('ex6', sa.Float(), nullable=True),
    sa.Column('ex7', sa.Float(), nullable=True),
    sa.Column('ex8', sa.Float(), nullable=True),
    sa.Column('ex9', sa.Float(), nullable=True),
    sa.Column('ex10', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('users',
    sa.Column('uid', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('username', sa.Text(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('last_date_license', sa.DateTime(timezone=True), nullable=True),
    sa.Column('allow_access', sa.Boolean(), nullable=True),
    sa.Column('name_trainings', sa.Text(), nullable=True),
    sa.Column('name_exer_train1', sa.Text(), nullable=True),
    sa.Column('name_exer_train2', sa.Text(), nullable=True),
    sa.Column('name_exer_train3', sa.Text(), nullable=True),
    sa.Column('name_exer_train4', sa.Text(), nullable=True),
    sa.Column('name_exer_train5', sa.Text(), nullable=True),
    sa.Column('array_shop_list', sa.ARRAY(sa.UUID()), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('training_all',
    sa.Column('uid', sa.Uuid(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('train1_uid', sa.Uuid(), nullable=True),
    sa.Column('train2_uid', sa.Uuid(), nullable=True),
    sa.Column('train3_uid', sa.Uuid(), nullable=True),
    sa.Column('train4_uid', sa.Uuid(), nullable=True),
    sa.Column('train5_uid', sa.Uuid(), nullable=True),
    sa.Column('index_train', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['train1_uid'], ['train1.uid'], ),
    sa.ForeignKeyConstraint(['train2_uid'], ['train2.uid'], ),
    sa.ForeignKeyConstraint(['train3_uid'], ['train3.uid'], ),
    sa.ForeignKeyConstraint(['train4_uid'], ['train4.uid'], ),
    sa.ForeignKeyConstraint(['train5_uid'], ['train5.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('training_all')
    op.drop_table('users')
    op.drop_table('train5')
    op.drop_table('train4')
    op.drop_table('train3')
    op.drop_table('train2')
    op.drop_table('train1')
    op.drop_table('shop_list')
    # ### end Alembic commands ###