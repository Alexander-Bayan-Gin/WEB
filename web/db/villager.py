from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from web.db.functions.database import Base


class Villager(Base):
    __tablename__ = 'villager'

    villager_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    church_id = Column(Integer, ForeignKey('human.church_id'))

    human_id = relationship("Human", back_populates="villager_num", uselist=False)
    occupation_num = relationship("Occupation", secondary='villager_occupation', back_populates="villager_num")
