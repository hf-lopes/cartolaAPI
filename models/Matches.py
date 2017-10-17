from models.BaseModel import Base


class Match(Base):

    __tablename__ = 'Match'
    match_week = Column(Integer, nullable = False)
    home_team_id = Column(Integer, ForeignKey('team.id')
    visiting_team_id= Column(Integer, ForeignKey('team.id')
    home_score = Column(Integer, nullable = False)
    visiting_score = Column(Integer, nullable = False)
    result = Column(String, nullable = False)
    year = Column(Integer, nullable = False, default=2014)


