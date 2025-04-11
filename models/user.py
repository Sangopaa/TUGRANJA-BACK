from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime


class User(Base):

    __tablename__ = "user"

    identifier = Column(Integer, primary_key=True, index=True)
    username = Column(String(200), unique=True, index=True)
    email = Column(String(200), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)

    farm_id = Column(
        Integer,
        ForeignKey("farm.identifier", name="fk_user_to_farm", ondelete="CASCADE"),
    )
    farm = relationship("Farm", foreign_keys=[farm_id])
