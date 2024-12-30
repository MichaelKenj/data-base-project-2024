"""Add color column to cars

Revision ID: 6260275b9bc8
Revises: 
Create Date: 2024-12-30 19:33:00.842941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6260275b9bc8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Добавляем новую колонку color к таблице cars
    op.add_column('cars', sa.Column('color', sa.String(), nullable=True))

def downgrade() -> None:
    # Убираем колонку color в случае отката
    op.drop_column('cars', 'color')