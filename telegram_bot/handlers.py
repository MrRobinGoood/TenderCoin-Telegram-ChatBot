import shutil
from asyncio import sleep

from aiogram import Bot, Router
from aiogram import F
from aiogram.types import Message


router = Router()


@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я <b>TenderCoin</b> бот - умный помощник для работы с электронными торгами.", parse_mode="HTML")
