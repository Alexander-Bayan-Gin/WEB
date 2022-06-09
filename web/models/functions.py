from datetime import date
from enum import Enum
from pydantic import BaseModel


class SexModel(str, Enum):
    MALE = "M"
    FEMALE = "F"


class HumanModel(BaseModel):
    human_name: str
    sex: SexModel
    birthday: date
    capital: int
    user: int

    class Config:
        orm_mode = True


class ChildModel(BaseModel):
    parent_church_id_1: int
    parent_church_id_2: int
    seniority: int

    class Config:
        orm_mode = True


class LordModel(BaseModel):
    lord_id: int

    class Config:
        orm_mode = True


class HumanId(HumanModel):
    church_id: int


class UserModel(BaseModel):
    name: str
    password: int

    class Config:
        orm_mode = True


class UserId(UserModel):
    id: int
    active: bool
    admin: bool


class ChildId(ChildModel):
    church_id: int


class LordId(LordModel):
    church_id: int


class VillagerModel(HumanModel):
    villager_id: int

    class Config:
        orm_mode = True


class OccupationModel(BaseModel):
    profession: str

    class Config:
        orm_mode = True


class VillagerOccupationModel(VillagerModel, OccupationModel):
    experience: int

    class Config:
        orm_mode = True

