"""Add Columns to Comment

Revision ID: 8c977ea60a0d
Revises: dbb4f294c145
Create Date: 2017-11-04 20:45:15.115393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c977ea60a0d'
down_revision = 'dbb4f294c145'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('email', sa.String(length=50), nullable=True))
    op.add_column('comments', sa.Column('name', sa.String(length=50), nullable=True))
    op.create_index(op.f('ix_comments_email'), 'comments', ['email'], unique=True)
    op.create_index(op.f('ix_comments_name'), 'comments', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_name'), table_name='comments')
    op.drop_index(op.f('ix_comments_email'), table_name='comments')
    op.drop_column('comments', 'name')
    op.drop_column('comments', 'email')
    # ### end Alembic commands ###
