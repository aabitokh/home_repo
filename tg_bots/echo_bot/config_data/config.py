from dataclasses import dataclass
from dotenv import load_dotenv
import os 


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    load_dotenv()
    print(os.getenv("TOKEN"))
    return Config(tg_bot=TgBot(token=os.getenv("TOKEN")))