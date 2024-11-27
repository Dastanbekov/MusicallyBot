from aiogram.filters.state import StatesGroup, State

class Youtube(StatesGroup):
    link_to = State()

class Admin(StatesGroup):
    mailing = State()