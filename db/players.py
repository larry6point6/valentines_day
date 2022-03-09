from sqlalchemy import Boolean, Column, Integer, Numeric, String
from sqlalchemy.sql.schema import ForeignKey

from db.base import Base


class Players(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    player_name = Column(String, nullable=False)
    game = Column(Numeric, nullable=False)
    time = Column(Numeric, nullable=False)
    goals = Column(Numeric, nullable=False)
    xG = Column(Numeric, nullable=False)
    assists = Column(Numeric, nullable=False)
    xA = Column(Numeric, nullable=False)
    shots_taken = Column(Numeric, nullable=False)
    key_passes = Column(Numeric, nullable=False)
    yellow_cards = Column(Numeric, nullable=False)
    red_cards = Column(Numeric, nullable=False)
    position = Column(Numeric, nullable=False)
    team_title = Column(String, ForeignKey("clubs.team"))
    npg = Column(Numeric, nullable=False)
    npxG = Column(Numeric, nullable=False)
    xGChain = Column(Numeric, nullable=False)
    xGBuildup = Column(Numeric, nullable=False)
