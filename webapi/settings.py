# -- coding: utf-8 --

from configparser import ConfigParser

def get_config():

    config = ConfigParser()

    config_file = "managemystuff.ini"

    read_config = config.read(config_file)

    if not read_config:
        return {}

    return config["default"]

default = get_config()

DB_HOST = default.get("DB_HOST", "db")
DB_PORT = default.get("DB_PORT", 28015)
DB_NAME = default.get("DB_NAME", "stuff")
