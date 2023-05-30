from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, BLOB, Text
from sqlalchemy.orm import relationship, Mapped

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, default=1)
    name = Column(Text)
    type = Column(Text)
    password = Column(Text)
    login = Column(Text, unique=True, index=True)

class TypeOfPayment(Base):
    __tablename__ = 'typesofpayments'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, default=1)
    name = Column(Text)
    description = Column(Text)
    
class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, index=True, primary_key=True, autoincrement=True, default=1)
    reason = Column(Text)
    
    userId = Column(Integer, ForeignKey(User.id))
    user = relationship("User", foreign_keys='Request.userId')
    typeId = Column(Integer, ForeignKey(TypeOfPayment.id))
    type = relationship('TypeOfPayment', foreign_keys='Payment.typeId')
    
class Request(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, autoincrement=True, default=1, index=True)
    name = Column(Text)
    userDescription = Column(Text)
    status = Column(Text)
    proof = Column(BLOB)
    userId = Column(Integer, ForeignKey(User.id))
    user = relationship("User", foreign_keys='Request.userId')