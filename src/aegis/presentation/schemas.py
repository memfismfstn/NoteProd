from pydantic import BaseModel, ConfigDict


class NoteCreate(BaseModel):
    title: str
    text: str


class NoteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    text:str
