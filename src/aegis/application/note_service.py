from aegis.domain.entities import Note
from aegis.domain.exception import NoteNotFound
from aegis.domain.repositories import NoteRepository


class NoteService:
    """Сервис заметок: сценарии использования (CRUD) поверх репозитория.

    Не знает о HTTP и способе хранения — работает только с абстракцией
    ``NoteRepository`` и переводит «пустые» результаты в доменные исключения.
    """

    def __init__(self,repo: NoteRepository)-> None:
        """Инициализирует сервис.

        Args:
            repo: Репозиторий, в котором хранятся заметки.
        """
        self._repo = repo

    def create(self, title: str, text: str)-> Note:
        """Создаёт новую заметку.

        Args:
            title: Заголовок заметки.
            text: Текст заметки.

        Returns:
            Созданная заметка с присвоенным идентификатором.
        """
        return self._repo.add(title=title, text=text)


    def get(self,note_id: int) -> Note:
        """Возвращает заметку по идентификатору.

        Args:
            note_id: Идентификатор заметки.

        Returns:
            Найденная заметка.

        Raises:
            NoteNotFound: Если заметки с таким идентификатором нет.
        """
        note = self._repo.get(note_id)
        if note is None:
            raise NoteNotFound(note_id)
        return note

    def list(self)-> list[Note]:
        """Возвращает все заметки.

        Returns:
            Список всех заметок (может быть пустым).
        """
        return self._repo.list()

    def delete(self, note_id: int)-> None:
        """Удаляет заметку по идентификатору.

        Args:
            note_id: Идентификатор удаляемой заметки.

        Raises:
            NoteNotFound: Если заметки с таким идентификатором нет.
        """
        if not self._repo.delete(note_id=note_id):
            raise NoteNotFound(note_id=note_id)