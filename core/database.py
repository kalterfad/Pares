from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.properties import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session = sessionmaker(bind=engine)

metadata = MetaData()
Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def test():
    for i in get_db():
        return i
