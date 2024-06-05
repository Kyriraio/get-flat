import asyncio

import logging
import time
from lib.flat_manager import getNewFlats
from aiogram import Bot, Dispatcher, types

TOKEN = "7333327630:AAFSaeL7N2mPhJl16rjEGSV0tn2XS2Jhkuw"

async def start_polling():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    users = set()

    @dp.message()
    async def search_flat(msg: types.Message):
        user_id = msg.from_user.id
        print (user_id)
        users.add(user_id)

        while True:
            if users:  # Проверяем, что есть пользователи для отправки
                for user_id in users:
                    # Отправляем сообщения каждому пользователю
                    for flat in getNewFlats():
                        await bot.send_message(user_id, flat)

            await asyncio.sleep(10)

    #543510374
    # Start polling
    await dp.start_polling(bot)

async def start():
    logging.basicConfig(level=logging.INFO)
    await start_polling()
