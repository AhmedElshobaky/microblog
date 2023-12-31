"""added language column to posts

Revision ID: 8415776b3ff0
Revises: 3cb13833ff01
Create Date: 2023-11-20 19:47:39.467547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8415776b3ff0'
down_revision = '3cb13833ff01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###
