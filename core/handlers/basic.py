from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import select_command, select_command3, select_command4
from core.keyboards.reply import reply_keyboard, keyboard_for_news_fir, keyboard_for_news
import surrogates
import requests
from bs4 import BeautifulSoup as Bs

count_news = 0


async def select_news(message: Message, bot: Bot):
    global count_news
    prov_news = True
    news_sp = parse()
    if len(news_sp) != 0:
        await message.answer(f"{news_sp[count_news]}", reply_markup=keyboard_for_news)
        count_news += 1
    else:
        await message.answer("Простите, новостей в данный момент нет",
                             reply_markup=reply_keyboard)
        prov_news = False
    if count_news >= len(news_sp) and prov_news:
        count_news = 0
        await message.answer("Вы пересмотрели все новости.", reply_markup=reply_keyboard)


async def ret(message: Message):
    await message.answer("Вы вышли из просмотра петомцев", reply_markup=reply_keyboard)


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
                         disable_web_page_preview=True, reply_markup=keyboard_for_news_fir)


async def contacts(message: Message):
    await message.answer(f'+7 (904) 364-23-15 - Администрация приюта\n'
                         f'<a href="https://vernost67.ru/contacts"> Дополнительная информация по поводу контактов </a>',
                         parse_mode="HTML", disable_web_page_preview=True)


async def about(message: Message):
    await message.answer(f'"Верность" - это приют и реабилитационный центр. Наш бот был разработан для более удобного '
                         f'поиска хозяев для животных, чтобы каждый из них смог найти вечно любящий дом. Мы хотим '
                         f'помочь приюту и спасти больше жизней❤. Подробности на<a href="https://vernost67.ru/"> '
                         f'сайте</a>', parse_mode="HTML", disable_web_page_preview=True)


def parse():
    final_sp = []
    url = 'https://vernost67.ru/news'
    main_class = 'post__text'

    try:
        req = requests.get(url)
        html = Bs(req.text, 'html.parser')
        t = html.find_all(class_=main_class)

    except Exception:
        print('Запрос не выполнен, проверьте подключение к интернету и корректность ссылки(((')
        t = []

    for el in t[:-2]:
        final_sp.append(' '.join(el.text.split()))
    return final_sp
