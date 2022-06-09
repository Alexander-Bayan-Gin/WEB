from sqlalchemy import *
from sqlalchemy.orm import relationship
from web.db.functions.database import Base


class Lord(Base):
    __tablename__ = 'lord'

    lord_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    church_id = Column(Integer, ForeignKey('human.church_id'))

    human_id = relationship("Human", back_populates="lord_num", uselist=False)
