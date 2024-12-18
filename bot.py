from aiogram import Bot, Dispatcher
import logging
import asyncio

from config import TOKEN   # Create if doesnt exist
from app.handlers.user.handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')

