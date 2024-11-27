from app.handlers.user.handlers import router
from aiogram.fsm.context import FSMContext

from aiogram import F
from aiogram.types import Message
from app.states import Admin

@router.message(F.text == 'Send message to all')
async def mailing(message:Message, state:FSMContext):
    await state.set_state(Admin.mailing)
    await message.answer('Send text:')

@router.message(Admin.mailing)
async def sending(message:Message, state:FSMContext):
    pass
