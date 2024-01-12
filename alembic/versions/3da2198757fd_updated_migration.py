"""Updated migration

Revision ID: 3da2198757fd
Revises: e8f1f2ad2344
Create Date: 2024-01-11 21:31:36.299270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3da2198757fd'
down_revision: Union[str, None] = 'e8f1f2ad2344'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
