from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

select_command = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Собака🐶",
            callback_data="1_dog"
        )
    ],
    [
        InlineKeyboardButton(
            text="Кошка🐱",
            callback_data="1_cat"
        )
    ]
])

select_command2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="С особенностями",
            callback_data="2_feature"
        )
    ],
    [
        InlineKeyboardButton(
            text="Без особенностей",
            callback_data="2_nofeature"
        )
    ],
    [
        InlineKeyboardButton(
            text="Не имеет значения",
            callback_data="2_dt_matter"
        )
    ]
])

select_command3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="🟣 Женский",
            callback_data="3_women"
        )
    ],
    [
        InlineKeyboardButton(
            text="🔵 Мужской",
            callback_data="3_men"
        )
    ],
    [
        InlineKeyboardButton(
            text="Не имeет значения",
            callback_data="3_dt_matter"
        )
    ]
])
select_command4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Ссылка",
            url="https://vernost67.ru/contacts"
        )
    ]
])
