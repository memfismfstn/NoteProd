from functools import lru_cache

from fastapi import Depends

from aegis.application.note_service import NoteService
from aegis.domain.repositories import NoteRepository
from aegis.infrastructure.in_memory_repo import InMemoryNoteRepository


@lru_cache
def get_repo()-> NoteRepository:
    return InMemoryNoteRepository()

def get_note_service(repo: NoteRepository = Depends(get_repo))-> NoteService:
    return NoteService(repo)
