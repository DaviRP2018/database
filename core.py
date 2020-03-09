"""Database core."""

import importlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.models import MyFollowers, MySelf
from database.settings import DB_STRING

Base = declarative_base()

class DatabaseSystem():
    """Main database system."""

    def __init__(self):
        """Init the database."""
        self.db = create_engine(DB_STRING)

    def create(self, obj_class):
        """Create tables in the database."""
        module = importlib.import_module("database.models")
        Model = getattr(module, obj_class)

        Session = sessionmaker(self.db)
        session = Session()

        Base.metadata.create_all(self.db)

        # Create
        model = Model(id=1, link="davi__rp")
        session.add(model)
        session.commit()

    def read(self):
        """Read tables."""
        Session = sessionmaker(self.db)
        session = Session()

        tables = session.query(MySelf)
        for table in tables:
            print(table.link)
