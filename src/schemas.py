from typing import List, NamedTuple, Optional


class NewExpenseMessage(NamedTuple):
    """Структура сообщения о новом расходе"""
    amount: int
    category_text: str


class Expense(NamedTuple):
    """Структура добавленного в БД нового расхода"""
    id: Optional[int]
    amount: int
    category_name: str
