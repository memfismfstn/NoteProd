from aegis.domain.entities import Note
from aegis.domain.exception import NoteNotFound
from aegis.domain.repositories import NoteRepository


class NoteService:
    def __init__(self,repo: NoteRepository)-> None:
        self._repo = repo

    def create(self, title: str, text: str)-> Note:
        return self._repo.add(title=title, text=text)


    def get(self,note_id: int) -> Note:
        note = self._repo.get(note_id)
        if note is None:
            raise NoteNotFound(note_id)
        return note

    def list(self)-> list[Note]:
        return self._repo.list()

    def delete(self, note_id: int)-> None:
        if not self._repo.delete(note_id=note_id):
            raise NoteNotFound(note_id=note_id)