from models.BaseModel import Base
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey


class Skill(Base):

    name = Column(String, nullable=False)
    nickname = Column(String, nullable = False)
    points = Column(Float, nullable = False)


