from models.BaseModel import Base


class Scout(Base):

    player_id = Column(Integer, ForeignKey('player.id')
    team_id = Column(Integer, ForeignKey('team.id')
    match_id = Column(Integer, ForeignKey('match.id')
    has_played = Column(Boolean, nullable=False)
    points = Column(Float, nullable = False)
    average_points = Column(Float, nullable = False)
    price = Column(Float, nullable = False)
    delta_price = Column(Float, nullable = False)
    home_game = Column(Boolean, nullable=False)
    score = Column(Float, nullable = False)
    plays = Column(ARRAY(Integer))
    year = Column(Integer, nullable=False, default=2014)


