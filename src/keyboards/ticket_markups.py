from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#------------------- Get Ticket Button -------------------
def get_ticket_btn():
    kb = ReplyKeyboardBuilder()

    kb.button(text='🆓 Get a ticket')
    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True,
                              one_time_keyboard=True)


#------------------- Get Main Menu Button -------------------
def to_main_menu():
    kb = ReplyKeyboardBuilder()

    kb.button(text='To the main menu➡️')
    kb.adjust(1)

    return kb.as_markup(resize_keyboard=True,
                              one_time_keyboard=False)