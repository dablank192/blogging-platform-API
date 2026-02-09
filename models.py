from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.expression import func, text
from database import Base
from sqlalchemy.dialects.postgresql import ARRAY

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key= True, nullable= False)
    title = Column(String, nullable= False)
    content = Column(String, nullable=False)
    category = Column(String, nullable=True)
    tags = Column(ARRAY(String), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable= False, server_default= text("now()"))
    updated_at = Column(DateTime(timezone=True), nullable= False, server_default= text("now()"))

