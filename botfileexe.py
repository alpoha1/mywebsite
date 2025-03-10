from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import asyncio

TOKEN = "7181435499:AAGIt6x49RYmSAbbCTwwIzILYU2qfRocO2k"  # Замените на свой токен бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Запустить бота", url=f"https://t.me/{(await bot.get_me()).username}")
    )
    await message.answer("Привет! Нажми на кнопку ниже, чтобы начать.", reply_markup=keyboard)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.delete_webhook())
    executor.start_polling(dp, skip_updates=True)
