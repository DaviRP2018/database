"""Database core."""

import importlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

from database.settings import DB_STRING

Base = declarative_base()

class DatabaseSystem():
    """Main database system."""

    def __init__(self):
        """Init the database."""
        self.db = create_engine(DB_STRING)

    def insert(self, Model, data):
        """Insert rows on a table or create it in the database."""
        if not data:
            raise Exception("Data can't be empty or null.")

        # module = importlib.import_module("database.models")
        # try:
        #     Model = getattr(module, Model)
        # except AttributeError:
        #     raise Exception("There is no such model")

        # if Model == MySelf:
        #     if self.get(Model):
        #         raise Exception("There can be only one instagram user.")

        Session = sessionmaker(self.db)
        session = Session()
        Base.metadata.create_all(self.db)

        max_id = session.query(func.max(Model.id))
        model = Model(id=max_id + 1, **data)
        session.add(model)
        session.commit()

    def get(self, Model):
        """Get tables."""
        # module = importlib.import_module("database.models")
        # Model = getattr(module, Model)

        Session = sessionmaker(self.db)
        session = Session()

        tables = session.query(Model)
        # for table in tables:
        #     print(table.link)
        return tables
