"""Initial migration

Revision ID: 194abc11ea14
Revises: 8a7b3932ecd3
Create Date: 2024-06-13 14:16:16.635928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '194abc11ea14'
down_revision: Union[str, None] = '8a7b3932ecd3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
