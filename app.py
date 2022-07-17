#!/usr/bin/env python3
import os
import logging
import monobank
import aiohttp
import schedule
import time

from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
MONOBANK_API_TOKEN = os.getenv("MONOBANK_API_TOKEN")

# If you need to connect using Proxy:
# if os.getenv("TELEGRAM_PROXY_URL") != "":
#     PROXY_URL = os.getenv("TELEGRAM_PROXY_URL")
#     PROXY_AUTH = aiohttp.BasicAuth(
#         login=os.getenv("TELEGRAM_PROXY_LOGIN"),
#         password=os.getenv("TELEGRAM_PROXY_PASSWORD")
#     )
# Initialize monobank API
mono = monobank.Client(token=MONOBANK_API_TOKEN)
currency_info = mono.get_currency()

# Initialize bot and dispatcher
#bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print("Bot AUTH = OK")
    print("Mono AUTH = OK" if currency_info != "" else "Mono AUTH = OUT")
    print("Now Currency Bot Online")
    print(currency_info)

#'''***************************************CLIENT****************************************'''
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Sends a welcome message and help on the bot"""
    await message.answer(
        "Привіт, user_name!\n\n"
        "Я вмію інформувати про курс валюти в Україні\n\n"
        "Курс на сьогодні: /today\n"
        "Курс який був вчора: /yesterday\n"
        "Отримувати курс щодня: /subscribe")

@dp.message_handler(commands=['today'])
async def today_rates(message: types.Message):
    """Sends a message with the current exchange rates for today"""
    await message.answer(
        "Привіт, user_name!\n\n"
        "Курс на сьогодні: {currency_info}\n\n"
        "Курс який був вчора: /yesterday\n"
        "Отримувати курс щодня: /subscribe")

@dp.message_handler(commands=['yesterday'])
async def yesterday_rates(message: types.Message):
    """Sends a message with the current exchange rates for today"""
    await message.answer(
        "Привіт, user_name!\n\n"
        "Курс який був вчора: {yesterday_rates}\n\n"
        "Курс на сьогодні: /today\n" 
        "Отримувати курс щодня: /subscribe")

@dp.message_handler(commands=['subscribe'])
async def send_thanks(message: types.Message):
    """Sends a message with the current exchange rates for today"""
    await message.answer(
        "Дякую за підписку!"
        )

@dp.message_handler() 
async def send_reply(message: types.Message):
    """Sends a reply message"""
    await message.answer(
        "Привіт, user_name!\n\n"
        "Я вмію інформувати про курс валюти в Україні\n\n"
        "Курс на сьогодні: /today\n"
        "Курс який був вчора: /yesterday\n"
        "Отримувати курс щодня: /subscribe")
#'''***************************************ADMIN*****************************************'''

# def db_load_currency_info():
#     print("I'm working...")
#     # block of recording currency rates in the database

# schedule.every().day.at("08:30").do(db_load_currency_info)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
#'''***************************************BOTH******************************************'''



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

