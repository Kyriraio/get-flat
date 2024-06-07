import asyncio
import datetime

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

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        while True:
            async with asyncio.Lock():
                if users:  # Проверяем, что есть пользователи для отправки
                    flats = getNewFlats()
                    print(f"{current_time} - {len(flats)} flats")
                    for user_id in users.copy():  # Делаем копию множества пользователей
                        for flat in flats:
                            await bot.send_message(user_id, flat)
                            print(f"{current_time} - {flat}")
                        #if(len(flats) == 0):
                        #    await bot.send_message(user_id, 'ыыыыыыыыы!!!')

            await asyncio.sleep(10 * 60)

    #543510374
    # Start polling
    await dp.start_polling(bot)

async def start():
    logging.basicConfig(level=logging.INFO)
    await start_polling()
