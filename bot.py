
import asyncio
from venv import logger

from internal.cmd.server.main import runer


CONFIG_FILE = "./.config/bot.ini"

if __name__ == "__main__":
    try:
        asyncio.run(runer(CONFIG_FILE))
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped")