import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from src.schemas import NewExpenseMessage, Expense
from src import expenses
from src import exceptions


logging.basicConfig(level=logging.INFO)
# API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
API_TOKEN = "5560662656:AAF-aqZ1gDEFYx1opVBtRqByyKsLQIAHcDk"

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


@dp.message_handler()
async def add_expense(message: types.Message):
    """Добавляет новый расход"""
    try:
        expense: Expense = expenses.add_expense(message.text)
    except exceptions.IncorrectMessage as e:
        return
    answer_message = (
        # f"Добавлены траты {expense.amount} руб на {expense.category_name}.\n\n"
        f"Добавлены траты {expense.amount} руб на {expense.category_text}.\n\n"
        # f"{expenses.get_today_statistics()}")
    )
    await message.answer(answer_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
