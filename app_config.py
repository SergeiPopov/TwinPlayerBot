import os
import logging

import environ

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(level=logging.INFO,
                    filename=f"{BASE_DIR}/bot.log",
                    filemode="w",
                    format="%(asctime)s %(filename)s/%(funcName)s %(levelname)s %(message)s")

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

TG_TOKEN = env('TG_TOKEN')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')
DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PASS = env('DB_PASS')

PG_DSN = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"