"""craete table

Revision ID: 64ca2660bfc9
Revises: 
Create Date: 2025-04-05 21:06:12.577734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '64ca2660bfc9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('questions_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], ),
    sa.ForeignKeyConstraint(['questions_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('games', sa.Column('title', sa.String(length=100), nullable=False))
    op.add_column('games', sa.Column('description', sa.String(length=1000), nullable=True))
    op.alter_column('games', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('games', 'start_time',
               existing_type=postgresql.TIME(),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.alter_column('games', 'end_time',
               existing_type=postgresql.TIME(),
               type_=sa.DateTime(),
               nullable=False)
    op.create_unique_constraint(None, 'games', ['title'])
    op.add_column('options', sa.Column('question_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'options', 'questions', ['question_id'], ['id'])
    op.alter_column('participations', 'start_time',
               existing_type=postgresql.TIME(),
               type_=sa.DateTime(),
               nullable=True)
    op.alter_column('participations', 'end_time',
               existing_type=postgresql.TIME(),
               type_=sa.DateTime(),
               existing_nullable=True)
    op.alter_column('questions', 'title',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=100),
               existing_nullable=False)
    op.alter_column('questions', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint('questions_options_id_fkey', 'questions', type_='foreignkey')
    op.drop_column('questions', 'options_id')
    op.alter_column('topics', 'name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=False)
    op.alter_column('users', 'birthdate',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'birthdate',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('topics', 'name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
    op.add_column('questions', sa.Column('options_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('questions_options_id_fkey', 'questions', 'options', ['options_id'], ['id'])
    op.alter_column('questions', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('questions', 'title',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
    op.alter_column('participations', 'end_time',
               existing_type=sa.DateTime(),
               type_=postgresql.TIME(),
               existing_nullable=True)
    op.alter_column('participations', 'start_time',
               existing_type=sa.DateTime(),
               type_=postgresql.TIME(),
               nullable=False)
    op.drop_constraint(None, 'options', type_='foreignkey')
    op.drop_column('options', 'question_id')
    op.drop_constraint(None, 'games', type_='unique')
    op.alter_column('games', 'end_time',
               existing_type=sa.DateTime(),
               type_=postgresql.TIME(),
               nullable=True)
    op.alter_column('games', 'start_time',
               existing_type=sa.DateTime(),
               type_=postgresql.TIME(),
               existing_nullable=False)
    op.alter_column('games', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('games', 'description')
    op.drop_column('games', 'title')
    op.drop_table('game_questions')
    # ### end Alembic commands ###
