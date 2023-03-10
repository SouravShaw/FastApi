from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqlite3
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# postgres
SQLALCHEMY_DATABASE_URL = "postgresql://rkqqfxku:YNXBP8bdJ85DEXcnLyChysZSQCH6StA9@tiny.db.elephantsql.com/rkqqfxku"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
