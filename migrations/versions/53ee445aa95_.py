"""empty message

Revision ID: 53ee445aa95
Revises: 5199ac2b07
Create Date: 2015-09-09 16:43:21.767401

"""

# revision identifiers, used by Alembic.
revision = '53ee445aa95'
down_revision = '5199ac2b07'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('story', sa.Column('external_id', sa.String(length=120), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('story', 'external_id')
    ### end Alembic commands ###