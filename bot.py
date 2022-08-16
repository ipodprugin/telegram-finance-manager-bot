import logging
import os

from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_greeting(message: types.Message):
    """Отправляет приветствие бота"""
    await message.answer(
        "Привет) Это бот для учёта расходов\n\n"
        "Добавить расход: 250 такси\n"
        "/today - сегодняшняя статистика\n"
        "/month - за текущий месяц\n"
        "/expenses - последние внесённые расходы\n"
        "/categories - категории трат")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
