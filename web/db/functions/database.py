from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from web.settings import settings

engine = create_engine(settings.database_url, connect_args={'check_same_thread': False})  # на каждый запрос новая сессия, подключения не прериспользуются

Session = sessionmaker(engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_session() -> Session:  # возвращяет в сессию
    session = Session()
    try:
        yield session
    finally:
        session.close()

