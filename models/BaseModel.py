from sqlalchemy.ext.declarative import declaritve_base
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime


class BaseModel(object):

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime, default = datetime.utcnow())

Base = declaritve_base(cls = BaseModel)