from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_password: str = ""
    database_username: str = ""
    database_address: str = ""
    database_port: int = 5432
    database: str = ""
    authorization_key: str = ""
    algorithm: str = ""
    acess_token_time: int = 30

    class Config:
        evn_file = "config/.env"

settings = Settings()
