import os
import asyncio

import environ
import telegram


async def main():
    env = environ.Env()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
    TG_TOKEN = env('TG_TOKEN')

    bot = telegram.Bot(TG_TOKEN)
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())