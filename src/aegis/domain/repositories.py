from abc import ABC, abstractmethod

from aegis.domain.entities import Note


class NoteRepository(ABC):

    @abstractmethod
    def add(self,title: str, text: str)-> Note: ...

    @abstractmethod
    def get(self,get_id: str)-> Note | None: ...

    @abstractmethod
    def list(self) -> list[Note]: ...

    @abstractmethod
    def delete(self, note_id:int) -> bool: ...

    