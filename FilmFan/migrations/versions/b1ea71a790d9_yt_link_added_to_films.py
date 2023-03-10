"""YT link added to films

Revision ID: b1ea71a790d9
Revises: c69d3355e395
Create Date: 2023-02-03 20:06:57.512402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1ea71a790d9'
down_revision = 'c69d3355e395'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.add_column(sa.Column('youtube_link', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.drop_column('youtube_link')

    # ### end Alembic commands ###
