"""empty message

Revision ID: 7735c545077e
Revises: 5d51e68cec54
Create Date: 2018-10-08 16:22:22.573717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7735c545077e'
down_revision = '5d51e68cec54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###