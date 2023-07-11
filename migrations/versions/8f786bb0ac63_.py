"""empty message

Revision ID: 8f786bb0ac63
Revises: 310e53e38b46
Create Date: 2023-07-06 11:34:59.532664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f786bb0ac63'
down_revision = '310e53e38b46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('username', name=op.f('uq_user_username'))
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), server_default='1', nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_question_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_question'))
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), server_default='1', nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name=op.f('fk_answer_question_id_question'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_answer_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_answer'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    op.drop_table('question')
    op.drop_table('user')
    # ### end Alembic commands ###