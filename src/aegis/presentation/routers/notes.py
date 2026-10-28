"""HTTP-эндпоинты для работы с заметками (префикс ``/notes``)."""
from fastapi import APIRouter, Depends, status

from aegis.application.note_service import NoteService
from aegis.presentation.dependencies import get_note_service
from aegis.presentation.schemas import NoteCreate, NoteOut

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(body: NoteCreate, service: NoteService = Depends(get_note_service)):
    """Создаёт заметку"""
    return service.create(body.title, body.text)


@router.get("", response_model=list[NoteOut])
def list_notes(service: NoteService = Depends(get_note_service)):
    """Возвращает список всех заметок"""
    return service.list()


@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int, service: NoteService = Depends(get_note_service)):
    """Возвращает заметку по идентификатору"""
    return service.get(note_id)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, service: NoteService = Depends(get_note_service)):
    """Удаляет заметку по идентификатору"""
    service.delete(note_id)