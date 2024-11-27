import os
import instaloader
from aiogram.types import Message, FSInputFile


async def clear_directory(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


async def download_and_send_instagram_media(message: Message):
    url = message.text
    await message.reply('Loading and Downloading your media from Instagram')

    download_path = f"downloads/{message.from_user.id}"
    os.makedirs(download_path, exist_ok=True)

    # Очищаем директорию перед загрузкой
    await clear_directory(download_path)

    loader = instaloader.Instaloader(dirname_pattern=download_path, filename_pattern="{shortcode}")

    loader.login('dastan.ait','2007aitik200712')
    try:
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        loader.download_post(post, target=download_path)

        media_file = None
        for file in os.listdir(download_path):
            if file.endswith((".jpg", ".mp4")):
                media_file = os.path.join(download_path, file)
                break
        from bot import bot
        if media_file:
            if media_file.endswith(".jpg"):
                await bot.send_photo(chat_id=message.chat.id, photo=FSInputFile(media_file))
            elif media_file.endswith(".mp4"):
                await bot.send_video(chat_id=message.chat.id, video=FSInputFile(media_file))

    except Exception as e:
        await message.reply(f'There is [ERROR] {e}')

async def download_and_send_instagram_video(message: Message):
    url = message.text
    await message.reply('Loading and Downloading your video from Instagram')

    download_path = f"downloads/{message.from_user.id}"
    os.makedirs(download_path, exist_ok=True)

    # Очищаем директорию перед загрузкой
    await clear_directory(download_path)

    loader = instaloader.Instaloader(dirname_pattern=download_path, filename_pattern="{shortcode}")

    try:
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])
        if post.is_video:
            loader.download_post(post, target=download_path)

            video_file = None
            for file in os.listdir(download_path):
                if file.endswith(".mp4"):
                    video_file = os.path.join(download_path, file)
                    break
            from bot import bot
            if video_file:
                await bot.send_video(chat_id=message.chat.id, video=FSInputFile(video_file))
        else:
            await message.reply('The provided link does not contain a video.')

    except Exception as e:
        await message.reply(f'There is [ERROR] {e}')