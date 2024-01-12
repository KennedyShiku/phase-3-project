# lib/database.py
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = "sqlite:///./smma.db"

engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base(metadata=MetaData())
Base.query = db_session.query_property()

def init_db():
    import lib.client
    import lib.content 
    import lib.marketer

    Base.metadata.create_all(bind=engine)
