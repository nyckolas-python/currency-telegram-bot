import os
import logging

import aiohttp
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
if os.getenv("TELEGRAM_PROXY_URL") != "":
	PROXY_URL = os.getenv("TELEGRAM_PROXY_URL")
	PROXY_AUTH = aiohttp.BasicAuth(
		login=os.getenv("TELEGRAM_PROXY_LOGIN"),
		password=os.getenv("TELEGRAM_PROXY_PASSWORD")
	)
ACCESS_ID = os.getenv("TELEGRAM_ACCESS_ID")

bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)

