"""creates rsvp, adds, allow_rsvp to proposal_space

Revision ID: 14d1424b47
Revises: 1c496c114b6
Create Date: 2015-01-30 16:09:42.434798

"""

# revision identifiers, used by Alembic.
revision = '14d1424b47'
down_revision = '1c496c114b6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rsvp',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('proposal_space_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rsvp_rsvp_action_enum', sa.Enum('M', 'N', 'Y'), nullable=False),
    sa.ForeignKeyConstraint(['proposal_space_id'], ['proposal_space.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'proposal_space_id'),
    sa.UniqueConstraint('user_id', 'proposal_space_id')
    )
    op.add_column(u'proposal_space', sa.Column('allow_rsvp', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'proposal_space', 'allow_rsvp')
    op.drop_table('rsvp')
    ### end Alembic commands ###
