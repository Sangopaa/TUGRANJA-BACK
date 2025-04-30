from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime


class Animal(Base):

    __tablename__ = "animal"

    identifier = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), unique=True, index=True)
    birth_date = Column(DateTime, nullable=False)
    race = Column(String(200), nullable=False)
    gender = Column(String(200), nullable=False)
    procedence = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)

    active = Column(Boolean, default=True)

    created_by = Column(
        Integer, ForeignKey("user.identifier", name="fk_user_creator_animal")
    )
    updated_by = Column(
        Integer, ForeignKey("user.identifier", name="fk_user_updater_animal")
    )
    group_id = Column(
        Integer,
        ForeignKey("group.identifier", name="fk_animal_to_group", ondelete="CASCADE"),
    )

    created_by_user = relationship("User", foreign_keys=[created_by])
    updated_by_user = relationship("User", foreign_keys=[updated_by])
    group = relationship("Group", foreign_keys=[group_id])
