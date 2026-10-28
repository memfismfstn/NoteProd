from aegis.domain.entities import Note
from aegis.domain.repositories import NoteRepository


class InMemoryNoteRepository(NoteRepository) :
    def __init__(self)-> None:
        self._items: dict[int, Note] = {}
        self._next_id: int = 1

    def add(self, title:str, text:str)-> Note:
        note = Note(id=self._next_id, title=title, text=text)
        self._items[note.id] = note
        self._next_id += 1
        return note



    def get(self, note_id:int) -> Note | None:
        return self._items.get(note_id)

    def list(self) -> list[Note]:
        return list(self._items.values())


    def delete(self, note_id)-> bool:
        return self._items.pop(note_id, None) is not None