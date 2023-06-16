from configs.database import Base, engine

def init():
    Base.metadata.create_all(bind=engine)