from sqlalchemy import *
from web.db.functions.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    name = Column(String, unique=True)
    password = Column(String)

    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    human_num = relationship("Human", back_populates="user_id", uselist=False)
