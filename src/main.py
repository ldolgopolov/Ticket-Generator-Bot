from aiogram import Bot, Dispatcher
from config import Config
import logging
from aiogram import F
import asyncio
from aiogram.filters import Command, CommandStart
from PIL import Image, ImageDraw, ImageFont

from handlers.user.start_actions import start
from ticket_generating.create_ticket import CreatePicture


async def main():
    logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=Config.token)
    dp = Dispatcher()

    image = Image.open(Config.image_path)
    bus_id = "22222"
    picture = CreatePicture(image, bus_id)
    picture.create_qrcode()
    picture.write_data()
    picture.generate_ticket()
    

    dp.message.register(start, CommandStart())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())