
import logging

from aiogram import Bot, Dispatcher

from internal.adaptors.handlers.base import BaseCom

from internal.adaptors.repo.repository import Repo
from pkg.config import config
from pkg.postgresql.connection import get_connection



# async def reg_middleware(dp, session ):
#     dp.middleware.setup(AuthMiddleware(session))

# TODO: РЕГИСТРАЦИЮ НУЖНО ДЕЛАТЬ НА УРОВЕНЬ РАНЬШЕ
async def reg_handlers(repo, cnf:config.Config):
    base = Dispatcher()
    com_start = BaseCom(repo)
    com_start.regisetr_handlers(base)


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

    try:
        await dp.start_polling(bot)
        logger.info("Starting bot")
    finally:
        # await dp.storage.close()
        # await dp.storage.wait_closed()
        # ses = await bot.get_session()
        # await ses.close()
        conn.close()
