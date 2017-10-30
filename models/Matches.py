from models.BaseModel import Base
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey, BigInteger

class Match(Base):

    match_week = Column(Integer, nullable = False)
    home_team_id = Column(BigInteger, ForeignKey('team.id'))
    visiting_team_id= Column(BigInteger, ForeignKey('team.id'))
    home_score = Column(Integer, nullable = False)
    visiting_score = Column(Integer, nullable = False)
    result = Column(String, nullable = False)
    year = Column(Integer, nullable = False, default=2014)


