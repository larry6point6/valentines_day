import pretty_errors
from sqlalchemy.orm.session import sessionmaker

from base import Base, Session, engine
from clubs import Clubs
from players import Players
from stats import Stats

Base.metadata.create_all(engine)

session = Session()

session.commit()
