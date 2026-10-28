from aegis.domain.entities import Note
from aegis.domain.repositories import NoteRepository


class InMemoryNoteRepository(NoteRepository):
    """Репозиторий заметок, хранящий данные в оперативной памяти процесса(бд нету просто).

    Реализация ``NoteRepository`` для разработки и тестов: данные теряются при
    перезапуске приложения и не разделяются между процессами. Потокобезопасность
    не гарантируется.

    Attributes:
        _items: Хранилище заметок в виде ``{id: Note}``.
        _next_id: Идентификатор, который получит следующая созданная заметка.
    """

    def __init__(self)-> None:
        """Создаёт пустое хранилище; нумерация идентификаторов начинается с 1."""
        self._items: dict[int, Note] = {}
        self._next_id: int = 1

    def add(self, title:str, text:str)-> Note:
        """Создаёт заметку с автоинкрементным идентификатором и сохраняет её.

        Args:
            title: Заголовок заметки.
            text: Текст заметки.

        Returns:
            Сохранённая заметка.
        """
        note = Note(id=self._next_id, title=title, text=text)
        self._items[note.id] = note
        self._next_id += 1
        return note



    def get(self, note_id:int) -> Note | None:
        """Возвращает заметку по идентификатору.

        Args:
            note_id: Идентификатор искомой заметки.

        Returns:
            Найденная заметка или ``None``.
        """
        return self._items.get(note_id)

    def list(self) -> list[Note]:
        """Возвращает копию списка всех заметок в порядке добавления.

        Returns:
            Список заметок (пустой, если заметок нет).
        """
        return list(self._items.values())


    def delete(self, note_id)-> bool:
        """Удаляет заметку по идентификатору.

        Args:
            note_id: Идентификатор удаляемой заметки.

        Returns:
            ``True``, если заметка существовала и была удалена, иначе ``False``.
        """
        return self._items.pop(note_id, None) is not None