from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import select_command, select_command3, select_command4
from core.keyboards.reply import reply_keyboard
import surrogates


async def idk(message: Message):
    await message.answer(f'Простите, я вас не понимаю.' + surrogates.decode("\U0001f972"))


async def reset(message: Message):
    await message.answer(f"Вы успешно сбросили клавиатуру", reply_markup=reply_keyboard)


async def call(message: Message):
    await message.answer(f"Контакты на странице сайта", reply_markup=select_command4)


async def th_chose(message: Message):
    await message.answer(f"Выберите пол питомца", reply_markup=select_command3)


async def pet(message: Message, bot: Bot):
    await message.answer(f"{message.from_user.first_name}, Выберите питомца", reply_markup=select_command)


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, F"Здравствуйте, {message.from_user.first_name}, рад вас видеть в"
                                                 F" нашем приюте.", reply_markup=reply_keyboard)
    await message.answer_sticker('CAACAgEAAxkBAAIE5GXOP6giDChxrSaNJ2QGW6OoIrmsAALxAQACOA6CEXTVKqzkcGAkNAQ')


async def get_sticker(message: Message, bot: Bot):
    await message.answer("Классный стикер, я его себе сохраню")
    await message.answer_sticker(message.sticker.file_id)


async def news(message: Message):
    await message.answer(f'<a href="https://vernost67.ru/news">- Сайт</a>\n<a '
                         f'href="https://t.me/vernostChannel">- Канал</a>\n Чтобы вы не пропустили ни одной новости о'
                         f' наших друзьях.', parse_mode="HTML",
                         disable_web_page_preview=True)


async def contacts(message: Message):
    await message.answer(f'+7 (904) 364-23-15 - Администрация приюта\n'
                         f'<a href="https://vernost67.ru/contacts"> Дополнительная информация по поводу контактов </a>',
                         parse_mode="HTML", disable_web_page_preview=True)


async def about(message: Message):
    await message.answer(f'"Верность" - это приют и реабилитационный центр. Наш бот был разработан для более удобного '
                         f'поиска хозяев для животных, чтобы каждый из них смог найти вечно любящий дом. Мы хотим '
                         f'помочь приюту и спасти больше жизней❤. Подробности на<a href="https://vernost67.ru/"> '
                         f'сайте</a>', parse_mode="HTML", disable_web_page_preview=True)
