from pydantic import BaseModel

class User(BaseModel):
    username: str
    date_joined: str
    location: str
    age: int