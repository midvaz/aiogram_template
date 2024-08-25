
import logging
import types

from aiogram import Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest


from internal.handlers.handler import Handler


logger = logging.getLogger(__name__)
# reg_c_data = CallbackData("register")


class BaseCom(Handler):
    def __init__(self, repo:Repo) -> None:
        super().__init__()
        self.repo= repo


    async def __start(self, m: Message) -> None:
        _ = await self.repo.user().add_user_id(m.from_user.id)

        await m.reply(
            text=start_text,
            reply=False,
            reply_markup=start_menu
        )