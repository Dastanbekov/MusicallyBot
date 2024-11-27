from aiogram.types import (InlineKeyboardButton,InlineKeyboardMarkup,
                           KeyboardButton,ReplyKeyboardMarkup)

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='YouTube downloader')],
    # [KeyboardButton(text='Instagram functions')],
    # [KeyboardButton(text='Pinterest downloader')]
])


#youtube keyboards
youTube_keyboard = InlineKeyboardMarkup(inline_keyboard= [
    [InlineKeyboardButton(text='Download Mp3', callback_data='youtube_mp3')],
    # [InlineKeyboardButton(text='Download Video', callback_data='youtube_video')]
])
