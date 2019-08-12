from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Event(Base):
	__tablename__ = 'event'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	start = Column(DateTime)
	end = Column(DateTime)
	desc = Column(String)
	image = Column(String)

class Member(Base):
	__tablename__ = 'member'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	desc = Column(String)
	image = Column(String)

class Image(Base):
	__tablename__ = 'image'
	id = Column(Integer, primary_key=True)
	filename = Column(String)


