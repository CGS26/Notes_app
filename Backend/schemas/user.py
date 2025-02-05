from fastapi import Form
from pydantic import BaseModel, ConfigDict

class RefreshTokenDTO(BaseModel):
    model_config = ConfigDict(extra='allow')

    refresh_token: str

    
class UserCreateDTO(BaseModel):
    model_config = ConfigDict(extra='allow')

    username:str
    full_name:str
    password:str

    # class Config:
    #     from_attributes=True

