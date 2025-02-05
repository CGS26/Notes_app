from pydantic import BaseModel, ConfigDict
from datetime import datetime

class NoteCreateDTO(BaseModel):
    model_config = ConfigDict(extra='allow')

    # user_id:int
    title: str
    body: str

class NoteUpdateDTO(BaseModel):
    model_config = ConfigDict(extra='allow')
    title: str
    body: str
    note_id: int

class NoteResponseDTO(BaseModel):
    model_config = ConfigDict(extra='allow')

    note_id: int
    title: str
    body: str
    modified_at: datetime
    created_at: datetime
    user_id: int

