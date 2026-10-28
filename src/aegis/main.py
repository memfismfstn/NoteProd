from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from aegis.domain.exception import NoteNotFound
from aegis.presentation.routers import notes

app = FastAPI(
    title = 'notes',
    docs_url='/'
)
app.include_router(notes.router)\

@app.exception_handler(NoteNotFound)
def note_not_found_handler(request: Request, exc: NoteNotFound):
    return JSONResponse(status_code=404, content={"detail": str(exc)})