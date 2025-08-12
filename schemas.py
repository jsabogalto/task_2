from pydantic import BaseModel
from typing import List

class PostBase(BaseModel):
    title: str
    body: str
    userId: int

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    title: str
    body: str

class Post(PostBase):
    id: int
    class Config:
        orm_mode = True

class PostTitles(BaseModel):
    title : str
    class Config:
        orm_mode = True
