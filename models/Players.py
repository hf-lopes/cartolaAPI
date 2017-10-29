from models.BaseModel import Base
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey


class Player(Base):

    name = Column(String, nullable = False)
    team_id = Column(Integer, ForeignKey('team.id'))
    position_id = Column(Integer, ForeignKey('position.id'))
    year = Column(Integer, nullable=False, default=2014)

