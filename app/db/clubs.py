from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import relationship

from db.base import Base
from db.players import Players


class Clubs(Base):
    __tablename__ = "clubs"

    team = Column(Numeric, nullable=False, primary_key=True)
    position = Column(String, nullable=False)
    matches = Column(Numeric, nullable=False)
    wins = Column(Numeric, nullable=False)
    draws = Column(Numeric, nullable=False)
    loses = Column(Numeric, nullable=False)
    goals_scored = Column(Numeric, nullable=False)
    goals_conceded = Column(Numeric, nullable=False)
    pts = Column(Numeric, nullable=False)
    xG = Column(Numeric, nullable=False)
    xG_diff = Column(Numeric, nullable=False)
    npxG = Column(Numeric, nullable=False)
    xGA = Column(Numeric, nullable=False)
    xGA_diff = Column(Numeric, nullable=False)
    npxGA = Column(Numeric, nullable=False)
    npxGD = Column(Numeric, nullable=False)
    ppda_coef = Column(Numeric, nullable=False)
    oppda_coef = Column(Numeric, nullable=False)
    deep = Column(Numeric, nullable=False)
    deep_allowed = Column(Numeric, nullable=False)
    xpts = Column(Numeric, nullable=False)
    xpts_dif = Column(Numeric, nullable=False)
    players = relationship("Players", backref="clubs")
