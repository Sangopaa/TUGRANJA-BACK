from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from models.base import Base
from datetime import datetime


class AnimalVariableValue(Base):

    __tablename__ = "animal_variable_value"

    identifier = Column(Integer, primary_key=True, index=True)
    value = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.now)

    created_by = Column(
        Integer,
        ForeignKey("user.identifier", name="fk_user_creator_animal_variable_value"),
    )
    updated_by = Column(
        Integer,
        ForeignKey("user.identifier", name="fk_user_updater_animal_variable_value"),
    )
    animal_id = Column(
        Integer,
        ForeignKey(
            "animal.identifier",
            name="fk_animal_variable_value_to_animal",
            ondelete="CASCADE",
        ),
    )
    variable_id = Column(
        Integer,
        ForeignKey(
            "variable.identifier",
            name="fk_animal_variable_value_to_variable",
            ondelete="CASCADE",
        ),
    )

    created_by_user = relationship("User", foreign_keys=[created_by])
    updated_by_user = relationship("User", foreign_keys=[updated_by])
    animal = relationship("Animal", foreign_keys=[animal_id])
    variable = relationship("Variable", foreign_keys=[variable_id])
