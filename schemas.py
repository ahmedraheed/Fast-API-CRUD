from typing import Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str 
    # published:Optional[bool]

class Showblog(BaseModel):
    title:str
    body:str

    class config():
        orm_mode=True

 
class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str


class login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None