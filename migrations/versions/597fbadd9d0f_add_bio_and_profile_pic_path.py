"""add bio and profile pic path

Revision ID: 597fbadd9d0f
Revises: 7593b3f978e1
Create Date: 2020-01-15 04:04:21.007054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '597fbadd9d0f'
down_revision = '7593b3f978e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
