from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from web.db.human import Human
from web.db.child import Child
from web.db.lord import Lord
from web.db.occupation import Occupation
from web.db.villager import Villager
from web.db.villager_occupation import VillagerOccupation
from web.user.models.usermodels import User
import pydantic


from web.db.functions.database import get_session
from web.models.functions import *


class Service:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get_human(self, human_id: int):
        this_id = (self.session.query(Human).filter_by(church_id=human_id).first())
        if not this_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return this_id

    def create(self, table_data: HumanModel):
        new_table_data = Human(**table_data.dict())  # распаковываем словарь в аргументы конструктора
        self.session.add(new_table_data)
        self.session.commit()
        return new_table_data

    def read(self, table_id):

        if table_id == "Human":
            table_data = (self.session.query(Human).all())
        elif table_id == "Child":
            table_data = (self.session.query(Child).all())
        elif table_id == "Lord":
            table_data = (self.session.query(Lord).all())
        elif table_id == "Villager":
            table_data = (self.session.query(Villager).all())
        elif table_id == "Occupation":
            table_data = (self.session.query(Occupation).all())
        elif table_id == "VillagerOccupation":
            table_data = (self.session.query(VillagerOccupation).all())
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return table_data

    def update(self, human_id: int, table_data: HumanModel):
        human = self._get_human(human_id)
        for field, value in table_data:
            setattr(human, field, value)
        self.session.commit()
        return human

    def delete(self, human_id: int):
        human = self._get_human(human_id)
        self.session.delete(human)
        self.session.commit()

    def reg(self, username: str, password: int, table_data: UserModel):
        this_id = (self.session.query(User).filter_by(name=username).first())
        if this_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        else:
            new_table_data = User(**table_data.dict())  # распаковываем словарь в аргументы конструктора
            self.session.add(new_table_data)
            self.session.commit()
            return new_table_data


