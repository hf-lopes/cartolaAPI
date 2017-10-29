from sqlalchemy.ext.declarative import api
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from sqlalchemy import Column, Integer, Boolean, Float, ARRAY, DateTime


class BaseModel(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime, default = datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


Base = api.declarative_base(cls=BaseModel)