from aiogram import Bot
from aiogram.types import Message


async def get_true_contact(message: Message, bot: Bot, phone: str):
    await message.answer(f"Вы отправили <b>свой</b> контиакт {phone}.")


async def get_fake_contact(message: Message, bot: Bot):
    await message.answer(f"Вы отправили не <b>свой</b> контакт.", parse_mode="HTML")
