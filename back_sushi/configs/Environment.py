from pydantic import BaseSettings
from functools import lru_cache

class EnvironmentSettings(BaseSettings):
    APP_NAME: str
    DATABASE_FILE: str

@lru_cache
def get_environment_variables():
    return EnvironmentSettings() 
#For avoid minor performance when call repeat many times.