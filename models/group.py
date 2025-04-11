from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime


class Group(Base):

    __tablename__ = "group"

    identifier = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)
    active = Column(Boolean, default=True)

    created_by = Column(
        Integer, ForeignKey("user.identifier", name="fk_user_creator_group")
    )
    updated_by = Column(
        Integer, ForeignKey("user.identifier", name="fk_user_updater_group")
    )
    farm_id = Column(
        Integer,
        ForeignKey("farm.identifier", name="fk_group_to_farm", ondelete="CASCADE"),
    )

    created_by_user = relationship("User", foreign_keys=[created_by])
    updated_by_user = relationship("User", foreign_keys=[updated_by])
    farm = relationship("Farm", foreign_keys=[farm_id])
