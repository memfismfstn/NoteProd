from dataclasses import dataclass


@dataclass
class Note:
    """Доменная сущность «Заметка».

    Чистая структура данных без зависимостей от фреймворка и хранилища.

    Attributes:
        id: Уникальный числовой идентификатор заметки (выдаётся репозиторием).
        title: Заголовок заметки.
        text: Основной текст заметки.
    """

    id: int
    title: str
    text: str