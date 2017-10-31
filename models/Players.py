from models.BaseModel import Base
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey, BigInteger
from sqlalchemy import UniqueConstraint

class Player(Base):

    name = Column(String, nullable = False)
    player_id = Column(BigInteger, nullable=False)
    team_id = Column(BigInteger, ForeignKey('team.id'))
    position_id = Column(BigInteger, ForeignKey('position.id'))
    year = Column(Integer, nullable=False, default=2014)
    __table_args__ = (UniqueConstraint('player_id', 'year', name='player_year_uid'),)
