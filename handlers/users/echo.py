from aiogram import types
from aiogram.types import ContentType, Message

from loader import dp


@dp.message_handler()
async def answer_message(message: types.Message):
    """Answer for simple message"""
    await message.answer("Не понял команды! 🤨😲")


@dp.message_handler(content_types=ContentType.PHOTO)
async def answer_photo(message: Message):
    """Answer for photo-message"""
    await message.answer("Я пока-что не принимаю фото! 🤨😲")
    print(message.photo[-1].file_id)
