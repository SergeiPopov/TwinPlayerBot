import os

import environ
from aiogram import Bot, Dispatcher


env = environ.Env()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
TG_TOKEN = env('TG_TOKEN')

dp = Dispatcher()
bot = Bot(token=TG_TOKEN)
