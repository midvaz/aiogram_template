
from aiogram import Router

from internal.handlers.base import BaseCom
from internal.config import config


async def reg_handlers( repo, cnf:config.Config):
    base_router = Router()
    com_start = BaseCom(repo)
    com_start.regisetr_handlers(base_router)

    return [base_router]


async def __reg_middleware(repo, dp, cnf:config.Config ):
    # dp.middleware.setup(AuthMiddleware(session))
    ...
