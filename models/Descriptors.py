from models.BaseModel import Base
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey, BigInteger
from sqlalchemy import UniqueConstraint

class Descriptors(Base):

    hash = Column(String, nullable = False)
    scout_id = Column(BigInteger, ForeignKey('scout.id'))
    feature_array = Column(ARRAY(Float))

    def __repr__(self):
        return "<Feature(name='%s' refers to scout=%s)>" % (self.name, self.scout_id)
