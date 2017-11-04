"""Add Relationship to Blog

Revision ID: 3c8c45e678c6
Revises: 8c977ea60a0d
Create Date: 2017-11-04 22:06:37.389069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c8c45e678c6'
down_revision = '8c977ea60a0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_blog_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'blogs', ['blog_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_blog_id_fkey', 'comments', 'comments', ['blog_id'], ['id'])
    # ### end Alembic commands ###
