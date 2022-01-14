from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

engine = create_engine("sqlite:///football_stats.db", echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()
