from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.dispatcher.filters.command import CommandStart


basic_router = Router()

@basic_router.message(CommandStart())
async def on_start_command(message: types.Message):
    await message.answer("Start")
