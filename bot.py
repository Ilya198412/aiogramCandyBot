#Здесь создается бот и хранится его токен

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token='-')
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp)