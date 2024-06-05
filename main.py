import asyncio
import sqlite3
from lib.service.kufar import create_table as create_table_kufar
from lib.telegram import start as start_bot

database = 'flats.db'

async def main():
    sqlite3.connect(database)
    create_table_kufar()
    await start_bot()
    

if __name__ == '__main__':
    asyncio.run(main())