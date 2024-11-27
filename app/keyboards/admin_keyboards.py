from aiogram.types import (InlineKeyboardButton,InlineKeyboardMarkup,
                           KeyboardButton,ReplyKeyboardMarkup)

admin_main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Send message to all [all users]', )],
])


dispatch_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Accept', callback_data='accept')],
    [InlineKeyboardButton(text='Cancel', callback_data='cancel')],
])