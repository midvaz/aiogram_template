
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from internal.repositories.repository import Repo
from internal.main import reg_handlers
from internal.config import config
from pkg.postgresql.connection import get_connection


async def runer(CONFIG_FILE) -> None:
    logger: logging.Logger = logging.getLogger(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    cnf: config.Config = config.load_config(CONFIG_FILE)
    storage = MemoryStorage()

    bot = Bot(token=cnf.tg_data.token, parse_mode="HTML")
    dp = Dispatcher(
        storage=storage
    )
    
    conn = await get_connection(
        user=cnf.db_psql.user,
        password=cnf.db_psql.password,
        database=cnf.db_psql.database,
        host=cnf.db_psql.host,
        port=cnf.db_psql.port
    )

    repo = Repo(conn=conn)
    
    routers:list = await reg_handlers(repo, cnf)
    
    for router in routers:
        dp.include_router(router)

    try:
        await dp.start_polling(bot)
        logger.info("Starting bot")
    finally:
        # await dp.storage.close()
        # await dp.storage.wait_closed()
        # ses = await bot.get_session()
        # await ses.close()
        conn.close()
