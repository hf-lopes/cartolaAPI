from models.BaseModel import Base
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey

class Position(Base):

    name = Column(String, nullable=False)
    nickname = Column(String, nullable = False)
    year = Column(Integer, nullable=False, default=2014)


