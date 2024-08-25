import sys
import asyncpg

from pkg.config.config import Config


async def get_connection(cnf:Config):
    try:
        conn = await asyncpg.connect(
            user=cnf.db.user, password=cnf.db.password,
            database=cnf.db.database, host=cnf.db.host,
            port=cnf.db.port
        )
        asyncpg.create_pool()
        return conn
    except Exception as e:
        print(f"Error: {e}\n")
        # TODO: ВЫНЕСТИ СТОП В BOT.PY
        sys.exit ()