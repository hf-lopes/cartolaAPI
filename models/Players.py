from models.BaseModel import Base
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey, BigInteger


class Player(Base):

    name = Column(String, nullable = False)
    team_id = Column(BigInteger, ForeignKey('team.id'))
    position_id = Column(BigInteger, ForeignKey('position.id'))
    year = Column(Integer, nullable=False, default=2014)

