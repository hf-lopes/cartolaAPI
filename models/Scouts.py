from models.BaseModel import Base
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey, BigInteger
from sqlalchemy import ForeignKeyConstraint

class Scout(Base):

    player_id = Column(BigInteger, nullable=False)
    team_id = Column(BigInteger, ForeignKey('team.id'))
    match_week = Column(Integer, nullable=False)
    has_played = Column(Boolean, nullable=False)
    points = Column(Float, nullable = False)
    average_points = Column(Float, nullable = False)
    price = Column(Float, nullable = False)
    delta_price = Column(Float, nullable = False)
    plays = Column(ARRAY(Integer))
    year = Column(Integer, nullable=False, default=2014)
    __table_args__ = ( ForeignKeyConstraint(['player_id', 'year'], ['player.player_id', 'player.year']),)


