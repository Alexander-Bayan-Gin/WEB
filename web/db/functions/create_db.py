from web.db.functions.database import Base, engine
from web.db.human import Human
from web.db.child import Child
from web.db.lord import Lord
from web.db.occupation import Occupation
from web.db.villager import Villager
from web.db.villager_occupation import VillagerOccupation
from web.user.models.usermodels import User


def create_bd():
    Base.metadata.create_all(engine)


create_bd()
