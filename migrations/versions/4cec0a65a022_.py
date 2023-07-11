"""empty message

Revision ID: 4cec0a65a022
Revises: 332f8f34162a
Create Date: 2023-07-08 16:09:54.376079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cec0a65a022'
down_revision = '332f8f34162a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer_voter', schema=None) as batch_op:
        batch_op.alter_column('answer_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer_voter', schema=None) as batch_op:
        batch_op.alter_column('answer_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
