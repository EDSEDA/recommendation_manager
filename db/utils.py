
from sqlalchemy import create_engine, Column, Integer, ARRAY, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings
from grifon import config

DB_URL = f'{settings.DB_DIALECT}://{config.DB_URL}'

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

