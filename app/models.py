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
    
class HSRGame8(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    slug: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), unique=True, nullable=True)
    lightcone0: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    lightcone1: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    lightcone2: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    lightcone3: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    relic0: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    relic1: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    relic2: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    ornament0: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    ornament1: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    ornament2: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    bodystat: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    feetstat: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    spherestat: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    ropestat: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    substats: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    

class GenshinGame8(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    slug: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), unique=True, nullable=True)
    weapon0: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    weapon1: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    weapon2: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    weapon3: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    artifact0: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    artifact1: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    artifact2: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    artifact3: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    sandsstat: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    gobletstat: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    circletstat: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)
    substats: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=True)