from pydantic import BaseModel
from typing import Optional
class Users(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Don Quixote",
                "email": "donquixote@gmail.com",
                "password": "123456"
            }
        }