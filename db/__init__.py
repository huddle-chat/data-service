from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URI"))

Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = Session.query_property()
