import re

from src.schemas import NewExpenseMessage, Expense
from src import exceptions


def add_expense(raw_message: str) -> Expense:
    """Добавляет новую запись о расходе.
    Принимает на вход текст сообщения от пользователя"""
    parsed_message: NewExpenseMessage = _parse_message(raw_message)
    return parsed_message


def _parse_message(raw_message: str) -> NewExpenseMessage:
    """Парсит текст пришедшего сообщения о новом расходе в формате: 500 продукты"""
    amount_and_category = re.match(r"(\d+) (.*)", raw_message)
    if not amount_and_category:
        raise exceptions.IncorrectMessage(
            "Не могу понять сообщение. Напишите сообщение в формате, "
            "например:\n1500 метро"
        )

    amount: int = int(amount_and_category.group(1))
    category_text: str = amount_and_category.group(2).strip().lower()
    return NewExpenseMessage(amount=amount, category_text=category_text)
