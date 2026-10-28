class NoteNotFound(Exception):
    def __init__(self, note_id:id)-> None:
        super().__init__(f'Note: {note_id} not found')
        self.note_id = note_id

        