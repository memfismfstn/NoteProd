from abc import ABC, abstractmethod

from aegis.domain.entities import Note


class NoteRepository(ABC):
    """Абстрактный репозиторий заметок.

    Определяет контракт хранилища, от которого зависит слой приложения
    (инверсия зависимостей). Конкретные реализации лежат в ``infrastructure``.
    """

    @abstractmethod
    def add(self,title: str, text: str)-> Note:
        """Создаёт и сохраняет новую заметку.

        Args:
            title: Заголовок заметки.
            text: Текст заметки.

        Returns:
            Сохранённая заметка с присвоенным идентификатором.
        """
        ...

    @abstractmethod
    def get(self,get_id: str)-> Note | None:
        """Возвращает заметку по идентификатору.

        Args:
            get_id: Идентификатор искомой заметки.

        Returns:
            Найденная заметка или ``None``, если такой заметки нет.
        """
        ...

    @abstractmethod
    def list(self) -> list[Note]:
        """Возвращает все сохранённые заметки.

        Returns:
            Список заметок (пустой, если заметок нет).
        """
        ...

    @abstractmethod
    def delete(self, note_id:int) -> bool:
        """Удаляет заметку по идентификатору.

        Args:
            note_id: Идентификатор удаляемой заметки.

        Returns:
            ``True``, если заметка была найдена и удалена, иначе ``False``.
        """
        ...

