import datetime

from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    query)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)


class Entry(Base):
    __tablename__='entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text, lenght=255, unique=True, required=True)
    body = Column(Text)
    created = Column(DateTime, default=datetime.datetime.now())
    edited = Column(DateTime, default=datetime.datetime.now())

    @classmethod
    def all(class_):

        return

    @classmethod
    def by_id(cls, id, session=None):
        return session.query(cls)




