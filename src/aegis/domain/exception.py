class NoteNotFound(Exception):
    """Заметка с указанным идентификатором не найдена.

    Бросается слоем приложения (``NoteService``). В HTTP-ответ с кодом 404
    преобразуется обработчиком исключений в ``aegis.main``.

    Attributes:
        note_id: Идентификатор заметки, которую не удалось найти.
    """

    def __init__(self, note_id:id)-> None:
        """Создаёт исключение и формирует сообщение об ошибке.

        Args:
            note_id: Идентификатор ненайденной заметки.
        """
        super().__init__(f'Note: {note_id} not found')
        self.note_id = note_id

