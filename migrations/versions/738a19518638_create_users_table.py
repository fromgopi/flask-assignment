"""create users table

Revision ID: 738a19518638
Revises: 
Create Date: 2019-07-15 11:20:37.133196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '738a19518638'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('isAdmin', sa.BOOLEAN, nullable=False)
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
