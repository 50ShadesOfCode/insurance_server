from sqlalchemy import Column, Integer, Text

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    type = Column(Text)
    password = Column(Text)
    login = Column(Text, unique=True, index=True)

class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    userDescription = Column(Text)
    status = Column(Text)
    userId = Column(Integer)