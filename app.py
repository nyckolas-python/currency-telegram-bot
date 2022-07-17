import os
import logging

import aiohttp
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

# If you need to connect using Proxy:
# if os.getenv("TELEGRAM_PROXY_URL") != "":
# 	PROXY_URL = os.getenv("TELEGRAM_PROXY_URL")
# 	PROXY_AUTH = aiohttp.BasicAuth(
# 		login=os.getenv("TELEGRAM_PROXY_LOGIN"),
# 		password=os.getenv("TELEGRAM_PROXY_PASSWORD")
# 	)

# Initialize bot and dispatcher
#bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])


#'''***************************************CLIENT****************************************'''
async def send_welcome(message: types.Message):
    """Sends a welcome message and help on the bot"""
    await message.reply(
        "Привіт, user_name!\n\n"
        "Я вмію інформувати про курс валюти в Україні\n\n"
        "Курс на сьогодні: /today\n"
        "Курс який був вчора: /yesterday\n"
        "Отримувати курс щодня: /subscribe")
#'''***************************************ADMIN*****************************************'''
#'''***************************************BOTH******************************************'''


    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

