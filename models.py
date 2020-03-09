"""Models for the database system."""

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
association_table = Table(
    "association", Base.metadata,
    Column("myself_id", Integer, ForeignKey("myself.id")),
    Column("myfollowers_id", Integer, ForeignKey("myfollowers.id")))


class MySelf(Base):
    """Table for myself."""

    __tablename__ = "myself"
    id = Column(Integer, primary_key=True)
    link = Column(String)
    followers = relationship("MyFollowers", secondary=association_table)


class MyFollowers(Base):
    """Table for who is following me."""

    __tablename__ = "myfollowers"
    id = Column(Integer, primary_key=True)
