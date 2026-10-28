"""Pydantic-схемы HTTP API: валидация входящих данных и сериализация ответов.

Схемы описывают (контрактa) API и отделяют внешнее представление данных
от доменной сущности ``Note``.
"""
from pydantic import BaseModel, ConfigDict


class NoteCreate(BaseModel):
    """Тело запроса на создание заметки.

    Attributes:
        title: Заголовок заметки.
        text: Текст заметки.
    """

    title: str
    text: str


class NoteOut(BaseModel):
    """Представление заметки в ответах API.

    Строится напрямую из доменной сущности (``from_attributes=True``).

    Attributes:
        id: Идентификатор заметки.
        title: Заголовок заметки.
        text: Текст заметки.
    """

    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    text:str
