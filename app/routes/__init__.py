from aiogram import Dispatcher
from aiogram.dispatcher.router import Router

from .basic import basic_router

__all__ = ["register_routers"]


def register_routers(dispatcher: Dispatcher):
    master_router = Router()

    master_router.include_router(basic_router)

    dispatcher.include_router(master_router)
