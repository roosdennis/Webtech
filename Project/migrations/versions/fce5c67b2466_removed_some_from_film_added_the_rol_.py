"""Removed some from film, added the Rol Table

Revision ID: fce5c67b2466
Revises: 13f95545a544
Create Date: 2023-01-30 11:54:15.767256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fce5c67b2466'
down_revision = '13f95545a544'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rol',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('acteur_id', sa.Integer(), nullable=True),
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.Column('personage', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.add_column(sa.Column('regisseur_id', sa.Integer(), nullable=True))
        batch_op.drop_column('trailer')
        batch_op.drop_column('regiseur_id')
        batch_op.drop_column('wiki')
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('wiki', sa.TEXT(), nullable=True))
        batch_op.add_column(sa.Column('regiseur_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('trailer', sa.TEXT(), nullable=True))
        batch_op.drop_column('regisseur_id')

    op.drop_table('rol')
    # ### end Alembic commands ###
