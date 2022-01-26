from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import relationship

from db.base import Base
from db.players import Players


class Clubs(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True)
    club_name = Column(String)
    league = Column(String)
    xga = Column(Numeric)
    players = relationship("Players", backref="clubs")

    def __init__(self, club_name, league):
        self.club_name = club_name
        self.league = league
