"""creating-base-models

Revision ID: 83ff9fdec492
Revises: 
Create Date: 2025-04-11 01:36:48.600662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83ff9fdec492'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('farm',
    sa.Column('identifier', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('identifier')
    )
    op.create_index(op.f('ix_farm_identifier'), 'farm', ['identifier'], unique=False)
    op.create_index(op.f('ix_farm_name'), 'farm', ['name'], unique=False)
    op.create_table('user',
    sa.Column('identifier', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('farm_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['farm_id'], ['farm.identifier'], name='fk_user_to_farm', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('identifier')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_identifier'), 'user', ['identifier'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('animal',
    sa.Column('identifier', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=False),
    sa.Column('race', sa.String(length=200), nullable=False),
    sa.Column('gender', sa.String(length=200), nullable=False),
    sa.Column('procedence', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.identifier'], name='fk_user_creator_animal'),
    sa.ForeignKeyConstraint(['updated_by'], ['user.identifier'], name='fk_user_updater_animal'),
    sa.PrimaryKeyConstraint('identifier')
    )
    op.create_index(op.f('ix_animal_identifier'), 'animal', ['identifier'], unique=False)
    op.create_index(op.f('ix_animal_name'), 'animal', ['name'], unique=True)
    op.create_table('group',
    sa.Column('identifier', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.Column('farm_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.identifier'], name='fk_user_creator_group'),
    sa.ForeignKeyConstraint(['farm_id'], ['farm.identifier'], name='fk_group_to_farm', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['updated_by'], ['user.identifier'], name='fk_user_updater_group'),
    sa.PrimaryKeyConstraint('identifier')
    )
    op.create_index(op.f('ix_group_identifier'), 'group', ['identifier'], unique=False)
    op.create_index(op.f('ix_group_name'), 'group', ['name'], unique=True)
    op.create_table('variable',
    sa.Column('identifier', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.identifier'], name='fk_user_creator_variable'),
    sa.ForeignKeyConstraint(['group_id'], ['group.identifier'], name='fk_variable_to_group', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['updated_by'], ['user.identifier'], name='fk_user_updater_variable'),
    sa.PrimaryKeyConstraint('identifier')
    )
    op.create_index(op.f('ix_variable_identifier'), 'variable', ['identifier'], unique=False)
    op.create_index(op.f('ix_variable_name'), 'variable', ['name'], unique=True)
    op.create_table('animal_variable_value',
    sa.Column('identifier', sa.Integer(), nullable=False),
    sa.Column('value', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.Column('animal_id', sa.Integer(), nullable=True),
    sa.Column('variable_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['animal_id'], ['animal.identifier'], name='fk_animal_variable_value_to_animal', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['created_by'], ['user.identifier'], name='fk_user_creator_animal_variable_value'),
    sa.ForeignKeyConstraint(['updated_by'], ['user.identifier'], name='fk_user_updater_animal_variable_value'),
    sa.ForeignKeyConstraint(['variable_id'], ['variable.identifier'], name='fk_animal_variable_value_to_variable', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('identifier')
    )
    op.create_index(op.f('ix_animal_variable_value_identifier'), 'animal_variable_value', ['identifier'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_animal_variable_value_identifier'), table_name='animal_variable_value')
    op.drop_table('animal_variable_value')
    op.drop_index(op.f('ix_variable_name'), table_name='variable')
    op.drop_index(op.f('ix_variable_identifier'), table_name='variable')
    op.drop_table('variable')
    op.drop_index(op.f('ix_group_name'), table_name='group')
    op.drop_index(op.f('ix_group_identifier'), table_name='group')
    op.drop_table('group')
    op.drop_index(op.f('ix_animal_name'), table_name='animal')
    op.drop_index(op.f('ix_animal_identifier'), table_name='animal')
    op.drop_table('animal')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_identifier'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_farm_name'), table_name='farm')
    op.drop_index(op.f('ix_farm_identifier'), table_name='farm')
    op.drop_table('farm')
    # ### end Alembic commands ###
