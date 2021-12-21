from aiogram import Dispatcher
from .throttling import ThrottlingMiddleware
from .blacklist import SetBlacklist


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(SetBlacklist())
