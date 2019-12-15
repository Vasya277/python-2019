"""empty message

Revision ID: 203357ce2e35
Revises: 50adf66055c8
Create Date: 2019-12-14 23:30:00.725692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '203357ce2e35'
down_revision = '50adf66055c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'admin')
    # ### end Alembic commands ###