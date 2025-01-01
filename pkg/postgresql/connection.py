import sys
import asyncpg

from internal.config.config import Config


async def get_connection(user :str, password :str, database :str, host :str, port :str):
    try:
        # TODO: НУЖНО ПЕРЕДАВАТЬ ИМЕННО ЗНАЧЕНИЕ, А НЕ КОНФ
        conn = await asyncpg.connect(
            user=user, password=password,
            database=database, host=host,
            port=port
        )
        asyncpg.create_pool()
        return conn
    except Exception as e:
        print(f"Error: {e}\n")
        # TODO: ВЫНЕСТИ СТОП В BOT.PY
        sys.exit ()