from sqlalchemy import *
from sqlalchemy.orm import relationship
from web.db.functions.database import Base


class Child(Base):
    __tablename__ = 'child'

    church_id = Column(Integer, ForeignKey('human.church_id'), unique=True, primary_key=True)
    parent_church_id_1 = Column(Integer, ForeignKey('human.church_id'))
    parent_church_id_2 = Column(Integer, ForeignKey('human.church_id'))
    seniority = Column(Integer, unique=True)

    child_id = relationship("Human", foreign_keys=[church_id], uselist=False)
    parent_1_id = relationship("Human", foreign_keys=[parent_church_id_1])
    parent_2_id = relationship("Human", foreign_keys=[parent_church_id_2])
