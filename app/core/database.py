from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:6512@localhost:3345/pares"
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