from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    is_bot = Column()
    first_name = Column()
    username = Column()
    last_name = Column()
    language_code = Column()
    can_join_groups = Column()
    can_read_all_group_messages = Column()
    supports_inline_queries = Column()
    date_joined = Column()

    def __repr__(self):
        return f"User {self.name}"
