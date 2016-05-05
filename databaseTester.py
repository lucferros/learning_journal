from pyramid import registry
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from learning_journal.models import Entry

engine = engine_from_config(registry.settings, 'sqlalchemy.')
Session = sessionmaker(bind=engine)

session = Session()
session.query(Entry).all()
