from aiogram import Bot
from aiogram.enums import ChatAction
from aiogram.types import Message
import asyncio


class Typing():
    def __init__(self, second):
        self.second = second

    async def send_typing_action(self, message: Message, bot: Bot):
        await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        await asyncio.sleep(self.second)