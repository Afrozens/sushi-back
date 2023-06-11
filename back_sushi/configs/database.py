# Crear el motor para conectarnos a nuestra bd.
from sqlalchemy import create_engine
# La sesión en SQLAlchemy es el objeto principal a través del cual las consultas y transacciones se coordinan con los recursos proporcionados por el Engine.
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from configs.Environment import get_environment_variables

# Runtime Environment Configuration
env = get_environment_variables()


SQLALCHEMY_DATABASE_URL = {f"sqlite:///{env.DATABASE_FILE}"}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()