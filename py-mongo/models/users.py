from pydantic import BaseModel

class Users(BaseModel):
    name: str
    email: str
    password: str