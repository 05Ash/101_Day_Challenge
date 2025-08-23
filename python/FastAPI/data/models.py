from pydoc import text
from sqlalchemy import TIMESTAMP, Column, Integer, String, Text, Boolean
from services.server import Base
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key = True, nullable = False)
    title = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    published = Column(Boolean, nullable = False, server_default = 'TRUE')
    created_at = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text('Now()'))
