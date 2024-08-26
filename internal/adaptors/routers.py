
from aiogram import Dispatcher

from internal.adaptors.handlers.base import BaseCom
from pkg.config import config

async def reg_handlers(repo, cnf:config.Config):
    base = Dispatcher()
    com_start = BaseCom(repo)
    com_start.regisetr_handlers(base)


async def reg_middleware(repo, dp, cnf:config.Config ):
    # dp.middleware.setup(AuthMiddleware(session))
    ...
