"""empty message

Revision ID: 447728ca6d2e
Revises: 14d1424b47
Create Date: 2015-04-06 16:43:50.255747

"""

# revision identifiers, used by Alembic.
revision = '447728ca6d2e'
down_revision = '14d1424b47'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('proposal_space', sa.Column('buy_tickets_url', sa.Unicode(length=250), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('proposal_space', 'buy_tickets_url')
    ### end Alembic commands ###
