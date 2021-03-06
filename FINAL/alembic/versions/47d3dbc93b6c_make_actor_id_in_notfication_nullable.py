"""make actor id in notfication nullable

Revision ID: 47d3dbc93b6c
Revises: 4c288143fd16
Create Date: 2014-11-20 04:04:13.837349

"""

# revision identifiers, used by Alembic.
revision = '47d3dbc93b6c'
down_revision = '4c288143fd16'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(u'chat', 'contact_name',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
    op.alter_column(u'chat', 'contact_read',
               existing_type=mysql.SMALLINT(display_width=6),
               nullable=False)
    op.alter_column(u'chat', 'owner_name',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
    op.alter_column(u'chat', 'owner_read',
               existing_type=mysql.SMALLINT(display_width=6),
               nullable=False)
    op.alter_column(u'notification', 'actor_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(u'notification', 'actor_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column(u'chat', 'owner_read',
               existing_type=mysql.SMALLINT(display_width=6),
               nullable=True)
    op.alter_column(u'chat', 'owner_name',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
    op.alter_column(u'chat', 'contact_read',
               existing_type=mysql.SMALLINT(display_width=6),
               nullable=True)
    op.alter_column(u'chat', 'contact_name',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
    ### end Alembic commands ###
