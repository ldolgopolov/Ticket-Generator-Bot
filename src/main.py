from aiogram import Bot, Dispatcher
from src.config import Config
import logging
from aiogram import F
import asyncio
from aiogram.filters import Command, CommandStart

from handlers.user.start_actions import start


async def main():
    logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=Config.token)
    dp = Dispatcher()

    

    dp.message.register(start, CommandStart())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())