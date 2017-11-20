from models.BaseModel import Base
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, String, ForeignKey, BigInteger
from sqlalchemy import UniqueConstraint

class Features(Base):

    name = Column(String, nullable = False)
    feature_query = Column(String, nullable=False)

    def __repr__(self):
        return "<Feature(name='%s', query=%s)>" % (self.name, self.feature_query)
