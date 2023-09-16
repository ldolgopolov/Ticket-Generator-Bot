from aiogram import Bot
from aiogram.types import Message


async def start(message: Message):
    if message.chat.type == 'private':
        user_name = str(message.from_user.first_name)
        user_sname = str(message.from_user.last_name)
        
        if user_sname == "None":
            await message.answer(f"Hello, <b>{user_name}🎉</b>", parse_mode='HTML')
        else:
            await message.answer(f"Hello, <b>{user_name} {user_sname}🎉</b>", parse_mode='HTML')
        