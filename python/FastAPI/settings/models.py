from pydoc import text
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Text, Boolean
from services.server import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    published = Column(Boolean, nullable = False, server_default = 'TRUE')
    created_at = Column(TIMESTAMP(timezone = True),
                        nullable = False,
                        server_default = text('Now()'))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable = False)
    user = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, nullable = False, primary_key = True)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone = True),
                        nullable = False,
                        server_default = text('NOW()'))
