"""create properties table

Revision ID: eda24bcb747d
Revises: 738a19518638
Create Date: 2019-07-15 11:33:16.758235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eda24bcb747d'
down_revision = '738a19518638'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'properties',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('type', sa.String(50), nullable=False),
        sa.Column('dimension', sa.String(50), nullable=False),
        sa.Column('createdBy', sa.Integer, sa.ForeignKey('users.id'), nullable=False)

    )
    pass


def downgrade():
    pass
