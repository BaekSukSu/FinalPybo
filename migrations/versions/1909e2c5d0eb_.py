"""empty message

Revision ID: 1909e2c5d0eb
Revises: f44fc1d0310c
Create Date: 2022-06-03 16:39:11.146329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1909e2c5d0eb'
down_revision = 'f44fc1d0310c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_question')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('_alembic_tmp_question',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('subject', sa.VARCHAR(length=200), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_question_user_id_user', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
