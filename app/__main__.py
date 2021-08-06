from pathlib import Path
import logging

from pydantic_loader.toml_config import load_toml
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

from config import AppConfig
from routes import register_routers


def main():
    config = load_toml(AppConfig, Path("config.toml"))

    logging.basicConfig(
        level=logging.INFO, 
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    fsm_storage = MemoryStorage()

    bot = Bot(token=config.bot.token, parse_mode="HTML")
    dispatcher = Dispatcher(storage=fsm_storage)

    register_routers(dispatcher)

    dispatcher.run_polling(bot)


if __name__ == "__main__":
    main()
