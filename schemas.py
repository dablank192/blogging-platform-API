from datetime import datetime
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    content: str
    category: str | None = None
    tags: list[str] | None = None

class Blog(BlogBase): #response format
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CreateBlog(BlogBase):
    pass