from aiogram.fsm.state import StatesGroup, State


class GetBusID(StatesGroup):
    GET_ID = State()
