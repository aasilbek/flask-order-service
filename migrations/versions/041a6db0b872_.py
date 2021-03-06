"""empty message

Revision ID: 041a6db0b872
Revises: 45205c48b129
Create Date: 2021-11-01 17:54:52.634850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '041a6db0b872'
down_revision = '45205c48b129'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###
