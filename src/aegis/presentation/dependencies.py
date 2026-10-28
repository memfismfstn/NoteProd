"""Зависимости FastAPI (``Depends``): сборка репозитория и сервиса.

Единственное место, где слой представления выбирает конкретную реализацию
репозитория (composition root).
"""
from functools import lru_cache
from fastapi import Depends

from aegis.application.note_service import NoteService
from aegis.domain.repositories import NoteRepository
from aegis.infrastructure.in_memory_repo import InMemoryNoteRepository


@lru_cache
def get_repo()-> NoteRepository:
    """Возвращает единый на всё приложение репозиторий заметок.

    Результат кэшируется через ``lru_cache``, поэтому все запросы работают
    с одним и тем же экземпляром (иначе in-memory данные не сохранялись бы
    между запросами).

    Returns:
        Экземпляр ``InMemoryNoteRepository``.
    """
    
    return InMemoryNoteRepository()

def get_note_service(repo: NoteRepository = Depends(get_repo))-> NoteService:
    """Создаёт сервис заметок для обработки одного запроса.

    Args:
        repo: Репозиторий, внедряемый через ``Depends(get_repo)``.

    Returns:
        ``NoteService``, работающий с переданным репозиторием.
    """

    return NoteService(repo)
