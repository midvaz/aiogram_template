
import logging

from aiogram import Bot, Dispatcher

from internal.adaptors.repo.repository import Repo
from internal.adaptors.routers import reg_handlers, reg_middleware
from pkg.config import config
from pkg.postgresql.connection import get_connection


async def runer(CONFIG_FILE):
    logger = logging.getLogger(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    cnf = config.load_config(CONFIG_FILE)
    # storage = MemoryStorage()

    bot = Bot(token=cnf.tg_data.token, parse_mode="HTML")
    dp = Dispatcher()
    
    conn = await get_connection(cnf)

    repo = Repo(conn=conn)
    
    await reg_handlers(repo, cnf)
    await reg_middleware(repo, dp, cnf)

    try:
        await dp.start_polling(bot)
        logger.info("Starting bot")
    finally:
        # await dp.storage.close()
        # await dp.storage.wait_closed()
        # ses = await bot.get_session()
        # await ses.close()
        conn.close()
