from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base

from datetime import datetime


class Farm(Base):
    __tablename__ = "farm"

    identifier = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
