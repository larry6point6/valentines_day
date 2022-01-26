from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from db.base import Base


class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"), unique=True)
    no_assists = Column(Integer)
    no_goals = Column(Integer)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)
    games_played = Column(Integer)
    average_rating = Column(Numeric(2, 2))

    def __init__(
        self,
        no_assists,
        no_goals,
        yellow_cards,
        red_cards,
        games_played,
        average_rating,
    ):
        self.no_assists = no_assists
        self.no_goals = no_goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.games_played = games_played
        self.average_rating = average_rating
