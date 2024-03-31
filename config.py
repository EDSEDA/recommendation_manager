from grifon.config import Settings as SharedSettings


class Settings(SharedSettings):
    ThisServiceField: int = 1

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
