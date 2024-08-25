import configparser
from dataclasses import dataclass


@dataclass
class Database:
    user: str
    password: str
    host: str
    database: str
    port: str

@dataclass
class Tg_data:
    token: str
    url: str

@dataclass
class Admins:
    id: tuple

@dataclass
class Config:
    db_psql:     Database
    tg_data:     Tg_data
    admin:       Tg_data


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    return Config(
        db_psql=Database(**config["db_postgresql"]),
        tg_data=Tg_data(**config["tg_bot"]),
        admin=Admins(**config["admins"])
    )