import sys
import asyncpg

from pkg.config.config import Config


async def get_connection(cnf:Config):
    try:
        # TODO: НУЖНО ПЕРЕДАВАТЬ ИМЕННО ЗНАЧЕНИЕ, А НЕ КОНФ
        conn = await asyncpg.connect(
            user=cnf.db_psql.user, password=cnf.db_psql.password,
            database=cnf.db_psql.database, host=cnf.db_psql.host,
            port=cnf.db_psql.port
        )
        asyncpg.create_pool()
        return conn
    except Exception as e:
        print(f"Error: {e}\n")
        # TODO: ВЫНЕСТИ СТОП В BOT.PY
        sys.exit ()