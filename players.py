from sqlalchemy import Boolean, Column, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from base import Base


class Players(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    club_id = Column(Integer, ForeignKey("clubs.id"))
    name = Column(String)
    age = Column(Integer)
    nationality = Column(String)
    value = Column(Numeric(10, 2))
    is_active_club = Column(Boolean)
    stats = relationship("Stats", backref="players", uselist=False)

    def __init__(self, name, age, nationality, value, is_active_club):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.value = value
        self.is_active_club = is_active_club
