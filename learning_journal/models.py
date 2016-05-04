
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode,
    DateTime,
    )

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


#class MyModel(Base):
#   __tablename__ = 'models'
#   id = Column(Integer, primary_key=True)
#   name = Column(Text)
#   value = Column(Integer)

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False, unique=True)
    body = Column(Text)
    created = Column(DateTime(timezone=True), default=func.now())
    edited = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, title, body):
        self.title = title
        self.body = body


    def all(self):
        pass

    def by_id(self, id):
        pass
    

Index('index', Entry.title, unique=True, mysql_length=255)
