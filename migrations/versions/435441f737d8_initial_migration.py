"""Initial migration

Revision ID: 435441f737d8
Revises: 
Create Date: 2024-11-04 00:36:57.118499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '435441f737d8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('completed_review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('annotations', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('csv_file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('department', sa.String(length=50), nullable=True),
    sa.Column('completed_courses', sa.String(length=150), nullable=True),
    sa.Column('experience_years', sa.Integer(), nullable=True),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('annotation_count', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('csv_file_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['csv_file_id'], ['csv_file.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('annotation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('annotation', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['review_id'], ['review.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('annotation')
    op.drop_table('review')
    op.drop_table('user')
    op.drop_table('csv_file')
    op.drop_table('completed_review')
    # ### end Alembic commands ###
