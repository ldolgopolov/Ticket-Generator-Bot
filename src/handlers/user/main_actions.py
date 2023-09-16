from aiogram import Bot
from aiogram.types import Message

from keyboards.ticket_markups import get_ticket_btn
from utils.typing_actions import Typing


async def start(message: Message, bot: Bot):
    if message.chat.type == 'private':
        user_name = str(message.from_user.first_name)
        user_sname = str(message.from_user.last_name)
        typing_1_sec = Typing(1)
        
        if user_sname == "None":
            await message.answer(f"Hello, <b>{user_name}</b>🤖", parse_mode='HTML')
        else:
            await message.answer(f"Hello, <b>{user_name} {user_sname}</b>🤖", parse_mode='HTML')

        await typing_1_sec.send_typing_action(message, bot)
        await message.answer('ℹ️ Due to the latest "innovations" from <b>Rīgas Satiksmes</b>, that after 21:00🕘 drivers check if people have tickets, but drivers cannot check the validity, I am the solution to generate a <b>fake ticket</b> for free🤫', parse_mode='HTML')
        await typing_1_sec.send_typing_action(message, bot)
        await message.answer("<b>The ticket you generated is not a real ticket</b>❗️", parse_mode='HTML', reply_markup=get_ticket_btn())


async def return_to_main_menu(message: Message):
    await message.answer('<b>Thank you for using</b>❤️', reply_markup=get_ticket_btn(), parse_mode='HTML')
        