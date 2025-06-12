import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

def getEnvVariable(key: str, defaultValue: str = None):
    value = os.getenv(key=key)
    if value is None:
        if defaultValue is None:
            raise EnvironmentError(f"{key} is not defined in environment variables")
        else:
            return defaultValue
    return value

logging.info("checking env variables")
DATABASE_URL = getEnvVariable("DATABASE_URL")