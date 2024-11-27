import os
from aiogram.types import Message
from aiogram.types import FSInputFile
import yt_dlp

async def download_and_send_mp3(message: Message):
    url = message.text
    await message.reply('Loading and Converting your mp3')

    download_path = f"downloads/{message.from_user.id}"
    os.makedirs(os.path.dirname(download_path), exist_ok=True)

    ydl_options = {
        'format': 'bestaudio/best',
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', 'audio')
            audio = FSInputFile(f'{download_path}/{title}.mp3')

            from bot import bot
            await bot.send_audio(chat_id=message.chat.id, audio=audio)

    except Exception as e:
        await message.reply(f'There is [ERROR] {e}')


