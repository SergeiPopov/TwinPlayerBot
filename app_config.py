import os
import logging

import environ


logging.basicConfig(level=logging.INFO, filename="bot.log", filemode="w")

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
TG_TOKEN = env('TG_TOKEN')