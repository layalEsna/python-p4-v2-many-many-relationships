"""add employee_meetings association table

Revision ID: b4ca40e90c0f
Revises: 4ffa431f1cb1
Create Date: 2024-11-28 20:45:18.212776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4ca40e90c0f'
down_revision = '4ffa431f1cb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees_meetings',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employees_meetings_employee_id_employees')),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], name=op.f('fk_employees_meetings_meeting_id_meetings')),
    sa.PrimaryKeyConstraint('employee_id', 'meeting_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees_meetings')
    # ### end Alembic commands ###
