from aiogram import Bot, Dispatcher
from config import Config
import logging
from aiogram import F
import asyncio
from aiogram.filters import Command, CommandStart

from handlers.user.get_ticket_actions import get_bus_id, send_ticket
from handlers.user.main_actions import return_to_main_menu, start
from handlers.admin.admin_notify import on_startup, on_shutdown
from utils.states.state_ticket import GetBusID


async def main():
    logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=Config.token)
    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.message.register(get_bus_id, F.text == '🆓 Get a ticket')
    dp.message.register(return_to_main_menu, F.text == 'To the main menu➡️')

    dp.message.register(send_ticket, GetBusID.GET_ID)

    dp.message.register(start, CommandStart())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())