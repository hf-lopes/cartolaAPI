from models.BaseModel import Base

class Team(Base):

    name = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    year = Column(Integer, nullable=False, default=2014)


