import os

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.context import FSMContext

from app.keyboards.keyboards import main_keyboard, youTube_keyboard
from app.keyboards.admin_keyboards import admin_main_keyboard
from app.states import Youtube
from app.utils.youtube_downloader import download_and_send_mp3
from config import ADMIN_ID as admin_id

router = Router()

@router.message(CommandStart())
async def start_main(message:Message):
    # if message.from_user.id != admin_id:
    await message.answer('Hello!', reply_markup=main_keyboard)  # change hello
    # await message.answer('Welcome admin!Choose what you want.', reply_markup= admin_main_keyboard)

#There starts youtube handlers
@router.message(F.text == 'YouTube downloader')
async def youtube_downloader(message:Message):
    await message.answer('[YouTube] Choose the option', reply_markup= youTube_keyboard)

#youtube commands

#there is starts yt audio download
@router.callback_query(F.data == 'youtube_mp3')
async def prompt_for_link(callback:CallbackQuery, state:FSMContext):
    await state.set_state(Youtube.link_to.state)
    await callback.message.answer("Please send me the YouTube link you want to download as mp3.")
@router.message(Youtube.link_to)
async def send_music(message:Message, state:FSMContext):
    await download_and_send_mp3(message)
    await state.clear()


#Youtube ends there !

