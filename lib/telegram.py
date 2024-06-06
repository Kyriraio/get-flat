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
            async with asyncio.Lock():
                if users:  # Проверяем, что есть пользователи для отправки
                    for user_id in users.copy():  # Делаем копию множества пользователей
                        flats = getNewFlats()
                        for flat in flats:
                            await bot.send_message(user_id, flat)
                            print(flat)
                        #if(len(flats) == 0):
                        #    await bot.send_message(user_id, 'ыыыыыыыыы!!!')

            await asyncio.sleep(10 * 60)

    #543510374
    # Start polling
    await dp.start_polling(bot)

async def start():
    logging.basicConfig(level=logging.INFO)
    await start_polling()
