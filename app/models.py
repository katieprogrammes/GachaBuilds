import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app import db
from typing import Optional

class Character(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    slug: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), unique=True, nullable=True)
    game: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)

    def __repr__(self):
        return f"Character('{self.id}', '{self.name}','{self.game}')"