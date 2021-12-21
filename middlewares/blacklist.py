import json

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


class SetBlacklist(BaseMiddleware):
    """Tracker of user last action"""
    async def on_process_message(self, message: types.Message, data: dict):

        user_id = message.from_user.id

        with open("blacklist.json", 'r', encoding='utf-8') as f:
            js_data = json.loads(f.read())

        if user_id in js_data["blacklist"]:
            raise CancelHandler()

    async def on_process_callback_query(self, cq: types.CallbackQuery, data: dict):
        user_id = cq.from_user.id
        message_text = str(data['callback_data'])

        with open("blacklist.json", 'r', encoding='utf-8') as f:
            js_data = json.loads(f.read())

        if user_id in js_data["blacklist"]:
            raise CancelHandler()
