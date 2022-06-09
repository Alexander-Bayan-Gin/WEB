from sqlalchemy import *
from web.db.functions.database import Base
from sqlalchemy.orm import relationship
from web.user.models.usermodels import User


class Human(Base):
    __tablename__ = 'human'

    church_id = Column(Integer, primary_key=True, autoincrement=True)
    human_name = Column(String)
    sex = Column(String)
    birthday = Column(Date)
    capital = Column(Integer)
    user = Column(Integer, ForeignKey("user.id"))

    user_id = relationship('User', back_populates="human_num", uselist=False)
    lord_num = relationship("Lord", back_populates="human_id", uselist=False)
    villager_num = relationship("Villager", back_populates="human_id", uselist=False)
