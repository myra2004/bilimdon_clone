"""updated

Revision ID: 133cb3b8c202
Revises: f92557f15652
Create Date: 2025-04-10 19:04:05.680120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '133cb3b8c202'
down_revision: Union[str, None] = 'f92557f15652'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_questions', sa.Column('question_id', sa.Integer(), nullable=False))
    op.drop_constraint('game_questions_questions_id_fkey', 'game_questions', type_='foreignkey')
    op.create_foreign_key(None, 'game_questions', 'questions', ['question_id'], ['id'])
    op.drop_column('game_questions', 'questions_id')
    op.alter_column('games', 'description',
               existing_type=sa.VARCHAR(length=1000),
               nullable=False)
    op.drop_constraint('games_title_key', 'games', type_='unique')
    op.alter_column('options', 'title',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=100),
               existing_nullable=False)
    op.drop_constraint('options_title_key', 'options', type_='unique')
    op.drop_column('options', 'updated_at')
    op.alter_column('questions', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint('questions_title_key', 'questions', type_='unique')
    op.drop_constraint('questions_game_id_fkey', 'questions', type_='foreignkey')
    op.drop_column('questions', 'game_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('game_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('questions_game_id_fkey', 'questions', 'games', ['game_id'], ['id'])
    op.create_unique_constraint('questions_title_key', 'questions', ['title'])
    op.alter_column('questions', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('options', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.create_unique_constraint('options_title_key', 'options', ['title'])
    op.alter_column('options', 'title',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
    op.create_unique_constraint('games_title_key', 'games', ['title'])
    op.alter_column('games', 'description',
               existing_type=sa.VARCHAR(length=1000),
               nullable=True)
    op.add_column('game_questions', sa.Column('questions_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'game_questions', type_='foreignkey')
    op.create_foreign_key('game_questions_questions_id_fkey', 'game_questions', 'questions', ['questions_id'], ['id'])
    op.drop_column('game_questions', 'question_id')
    # ### end Alembic commands ###
