from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from fastapi import Depends
from typing import Annotated


DATABASE_URL = "postgresql+pscopg2://muqaddas:2004@localhost:5432/delete"

engine = create_engine(DATABASE_URL)

session= sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


db_dep = Annotated[Session, Depends(get_db)]