
from sqlalchemy import (Column, DateTime,
                        Integer, String, Boolean, ForeignKey, Date, JSON, UniqueConstraint, Enum, Numeric,
                        BigInteger, Float)
from sqlalchemy import Index
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship, declared_attr, declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(String(), primary_key=True)
    name = Column(String())
    embedding = Column(ARRAY(Float), nullable=False, comment='Эмбеддинг юзера')
