from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from web.db.functions.database import Base


class Occupation(Base):
    __tablename__ = 'occupation'

    profession = Column(String, primary_key=True)

    villager_num = relationship("Villager", secondary='villager_occupation', back_populates="occupation_num")
