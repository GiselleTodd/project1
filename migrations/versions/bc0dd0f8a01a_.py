"""empty message

Revision ID: bc0dd0f8a01a
Revises: c2746fc61a0a
Create Date: 2020-04-08 12:44:42.325085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc0dd0f8a01a'
down_revision = 'c2746fc61a0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('datejoined', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'datejoined')
    # ### end Alembic commands ###