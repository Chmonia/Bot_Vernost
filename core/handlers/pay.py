from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Пожертвование через Telegarm бота",
        description="Мы будем очень благодарны, если вы пожертвуете на помощь приюту и животным :)",
        provider_token="381764678:TEST:79718",
        payload="Оплата через бота",
        currency="rub",
        prices=[
            LabeledPrice(
                label="На лакомства",
                amount=10000
            )
        ],
        max_tip_amount=500000,
        suggested_tip_amounts=[20000, 30000, 50000, 100000],
        start_parameter="",
        photo_url=None,
        provider_data=None,
        need_name=False,
        need_email=False,
        need_phone_number=True,
        need_shipping_address=False,
        allow_sending_without_reply=True,
        is_flexible=False,
        send_email_to_provider=False,
        send_phone_number_to_provider=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        reply_markup=None,
        request_timeout=10
    )


async def pre_checkout_query(pree_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pree_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = (f"Спасибо за помощь приюту {message.successful_payment.total_amount // 100}"
           f" {message.successful_payment.currency}")
    await message.answer(msg)
