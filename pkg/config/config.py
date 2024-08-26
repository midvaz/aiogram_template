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
class Deamon:
    istrue: bool

@dataclass
class Config:
    db_psql:     Database
    tg_data:     Tg_data


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)
    
    deamon = Deamon(**config["deamon"])
    if deamon.istrue == True:
        psql = "db_postgresql"
    else:
        psql = "db_postgresql_local"

    return Config(
        db_psql=Database(**config[psql]),
        tg_data=Tg_data(**config["tg_bot"]),
    )