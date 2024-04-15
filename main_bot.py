import asyncio

from aiogram import Bot, Dispatcher, F
import logging
from aiogram.dispatcher.filters import Command, ContentTypesFilter
from aiogram.types import ContentType
from dotenv import load_dotenv
from core.filters.iscintact import IsTrueContact
from core.handlers.basic import get_start, get_sticker, call, reset
from core.handlers.callback import select_pet, select_pet2, select_pet3, output_pets, all_pets
from core.handlers.contact import get_true_contact, get_fake_contact
from core.settings import settings
from core.utils.commands import set_commands
from core.handlers.basic import pet, news, contacts, about, idk
from core.handlers.pay import order, pre_checkout_query, successful_payment


dp = Dispatcher()


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, F"Бот запущен")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, F"Бот остановлен")


async def start():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(token=settings.bots.bot_token)

    dp.startup.register(start_bot)
    dp.callback_query.register(select_pet3, F.data.startswith("3_"))
    dp.callback_query.register(select_pet2, F.data.startswith("2_"))
    dp.callback_query.register(select_pet, F.data.startswith("1_"))
    dp.message.register(order, text="Благотворительость 💸")
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, ContentTypesFilter(content_types=[ContentType.SUCCESSFUL_PAYMENT]))
    dp.message.register(all_pets, text="Найденные питомцы 🌸")
    dp.message.register(all_pets, text="Показать следующего питомца:")
    dp.message.register(output_pets, text="Следующий питомец 🐶")
    dp.message.register(output_pets, text="Показать питомцев:")
    dp.message.register(call, text="Связаться с нами и забарть питомца 📞")
    dp.message.register(news, text="Новости 📱")
    dp.message.register(reset, commands="reset")
    dp.message.register(contacts, text="Связь с нами 📞")
    dp.message.register(about, text="О нас ❕")
    dp.message.register(pet, text="Забрать питомца 🐶")
    dp.message.register(get_true_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]), IsTrueContact())
    dp.message.register(get_fake_contact, ContentTypesFilter(content_types=[ContentType.CONTACT]))
    dp.shutdown.register(stop_bot)
    dp.message.register(get_sticker, F.content_type == ContentType.STICKER)
    dp.message.register(get_start, Command(commands=["start", "run", "старт"]))
    dp.message.register(idk)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
