from model import Base, Event, Image, Member

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///savetfp.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_event(title,start, end, descrip, picfile):
	"""
	Add a event to the database
	"""
	event = Event(name=title, start=start, end = end, desc=descrip,image=picfile)
	session.add(event)
	session.commit()


def query_event_name(name):
	"""
	Find the first student in the database,
	by their name
	"""
	event = session.query(Event).filter_by(
		name=name).first()
	return event

def query_events():
	"""
	Return all the events in the database.
	"""
	events = session.query(Event).all()
	return events


def delete_event(id):
	"""
	Delete all students with a certain id
	from the database.
	"""
	session.query(Event).filter_by(
		id=id).delete()
	session.commit()


def query_event_id(id):
    return session.query(Event).filter_by(
        id=id).first()

def query_images():
	"""
	Return all the images in the database.
	"""
	events = session.query(Image).all()
	return events

def add_image(picfile):
	"""
	Add a event to the database
	"""
	image = Image(filename=picfile)
	session.add(image)
	session.commit()

def delete_image(id):
	session.query(Image).filter_by(
		id=id).delete()
	session.commit()


def add_member(title, descrip, picfile):
	"""
	Add a event to the database
	"""
	member = Member(name=title, desc=descrip,image=picfile)
	session.add(member)
	session.commit()


def query_members():
	"""
	Return all the members in the database.
	"""
	events = session.query(Member).all()
	return events


def delete_member(id):
	"""
	Delete all students with a certain id
	from the database.
	"""
	session.query(Member).filter_by(
		id=id).delete()
	session.commit()