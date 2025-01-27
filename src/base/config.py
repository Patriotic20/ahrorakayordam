
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DB_USER: str 
    DB_HOST: str 
    DB_PASSWORD: str 
    DB_PORT: str 
    DB_NAME: str 
    # MODE: str

    # SECRET_KEY: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int
    # ALGORITHM: str

    @property
    def connection_string(self):
        return (
            f'postgresql+psycopg2://'
            f'{self.DB_USER}:'
            f'{self.DB_PASSWORD}@'
            f'{self.DB_HOST}:{self.DB_PORT}/'
            f'{self.DB_NAME}'
        )


    model_config = ConfigDict(env_file=".env")

settings = Settings()
