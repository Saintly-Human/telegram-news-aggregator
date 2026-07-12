import logging
import asyncio
from aiogram import Bot, Dispatcher
from environs import Env
from tg_bot.handlers.user.text import router as user_text_router
from tg_bot.handlers.user.callback import router as user_callback_router

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(user_text_router)
    dp.include_router(user_callback_router)

    await dp.start_polling(bot)


asyncio.run(main())