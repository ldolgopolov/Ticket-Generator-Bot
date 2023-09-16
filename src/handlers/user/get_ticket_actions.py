from aiogram import Bot
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from PIL import Image
from keyboards.ticket_markups import to_main_menu

from ticket_generating.create_ticket import CreatePicture
from utils.states.state_ticket import GetBusID
from config import Config


async def get_bus_id(message: Message, state: FSMContext):
    if message.chat.type == 'private':
        await message.answer("<b>Enter the ID (number) of the transport:</b>", parse_mode='HTML', reply_markup=ReplyKeyboardRemove())
        await state.set_state(GetBusID.GET_ID)


async def send_ticket(message: Message, bot: Bot, state: FSMContext):
    if message.chat.type == 'private':
        await state.update_data(bus_id=message.text)

        context_data = await state.get_data()
        bus_id = context_data.get('bus_id')

        sticker = await bot.send_sticker(message.chat.id, sticker="CAACAgIAAxkBAAEKPT5k-QYiWW9suC0AAbvsB3dMTI0z54wAAkEBAALNGzAI8fBiGN_2llgwBA")

        image = Image.open(Config.image_path)
        
        picture = CreatePicture(image, bus_id)
        picture.create_qrcode()
        picture.write_data()
        picture.generate_ticket()

        await state.clear()

        await bot.delete_message(message.chat.id, message_id=sticker.message_id)

        ticket = FSInputFile("ticket.jpg")
        await bot.send_photo(chat_id=message.chat.id, photo=ticket, caption="<b>Never show this ticket to the checker❗️\nThis ticket is not a working❗️</b>", parse_mode='HTML', reply_markup=to_main_menu())

        picture.delete_files("ticket.jpg")
