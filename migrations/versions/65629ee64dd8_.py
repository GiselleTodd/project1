"""empty message

Revision ID: 65629ee64dd8
Revises: 
Create Date: 2020-03-14 10:05:59.088738

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65629ee64dd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('bio', sa.String(length=150), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('profilephoto', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    # ### end Alembic commands ###
