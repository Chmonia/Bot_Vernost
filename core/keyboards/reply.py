from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Забрать питомца 🐶"
        ),
        KeyboardButton(
            text="Новости 📱"
        ),
        KeyboardButton(
            text="Связь с нами 📞")
    ],
    [
        KeyboardButton(
            text="О нас ❕"
        )
    ],
    [
        KeyboardButton(
            text="Найденные питомцы 🌸"
        ),
        KeyboardButton(
            text="Благотворительость 💸",
        )
    ]
], resize_keyboard=True, input_field_placeholder='Выберите кнопку')

reply_keyboard2 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Следующий питомец 🐶"
        )],
    [
        KeyboardButton(
            text="Связаться с нами и забарть питомца 📞"
        )
    ],
    [
        KeyboardButton(
            text="Выйти из показа питомцев"
        )]
], resize_keyboard=True, input_field_placeholder='Выберите кнопку')

reply_keyboard3 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Показать питомцев:"
        )]
], resize_keyboard=True, input_field_placeholder='Выберите кнопку')

reply_keyboard4 = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Показать следующего питомца:"
        )],
    [
        KeyboardButton(
            text="Выйти из показа питомцев"
        )]

], resize_keyboard=True, input_field_placeholder='Выберите кнопку')

keyboard_for_news = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Показать следующую новость:"
        )],
    [
        KeyboardButton(
            text="Выйти из показа питомцев"
        )]

], resize_keyboard=True, input_field_placeholder='Выберите кнопку')

keyboard_for_news_fir = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Показать новости не выходя из телеграмма 🐶"
        )]

], resize_keyboard=True, input_field_placeholder='Выберите кнопку')
