from sqlalchemy.ext.declarative import api
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, DateTime, BigInteger


class BaseModel(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(BigInteger, primary_key = True)
    created_at = Column(DateTime, default = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = Column(DateTime, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                                onupdate=datetime.utcnow().strftime('"%Y-%m-%d %H:%M:%S"'))


Base = api.declarative_base(cls=BaseModel)