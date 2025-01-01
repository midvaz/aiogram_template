import logging
import types

from aiogram import Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest

from internal.handlers.handler import Handler
from internal.repositories.repository import Repo
from internal.service.base.main import Base

logger = logging.getLogger(__name__)


class BaseCom(Handler):
    def __init__(self, repo:Repo) -> None:
        super().__init__()
        self.base = Base(repo)


    async def __start(self, m: Message) -> None:
        text = await self.base.start()

        await m.reply(
            text=text,
            reply=False,
        )


    def regisetr_handlers(self, dp: Dispatcher) -> None:
        dp.message.register(self.__start, Command("start"))
