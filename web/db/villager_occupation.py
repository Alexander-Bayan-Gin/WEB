from sqlalchemy import Column, Integer, String, ForeignKey
from web.db.functions.database import Base


class VillagerOccupation(Base):
    __tablename__ = 'villager_occupation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    villager_id = Column(Integer, ForeignKey('villager.villager_id'), nullable=False)
    villager_profession = Column(String, ForeignKey('occupation.profession'))
    experience = Column(Integer)


