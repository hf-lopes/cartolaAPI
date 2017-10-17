from models.BaseModel import Base


class Skill(Base):

    name = Column(String, nullable=False)
    nickname = Column(String, nullable = False)
    Points = Column(Float, nullable = False)


