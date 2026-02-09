
from operator import or_
from fastapi import FastAPI, Depends, Response, HTTPException, status
from database import get_db, Base, engine
import models
import schemas
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/blog", response_model= List[schemas.Blog])

def get_blog(db: Session = Depends(get_db), term: Optional[str] = None):
    finded_blog = db.query(models.Post)
    all_blog = finded_blog.all()

    if term:
        filtered_blog = finded_blog.filter(or_(
            models.Post.title.contains(term),
            models.Post.content.contains(term),
            models.Post.category.contains(term),
            models.Post.tags.contains([term])
        ))
        return filtered_blog
    return all_blog


@app.get("/blog/{id}")
def get_one_blog(id: int, db: Session = Depends(get_db)):
    blogs = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return blogs


@app.post("/blog/create", status_code= status.HTTP_201_CREATED)
def create_blog(blog: schemas.CreateBlog, db: Session = Depends(get_db)):
    new_blog = models.Post(**blog.model_dump())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put("/blog/update/{id}")
def update_blog(id: int, blog: schemas.CreateBlog, db: Session = Depends(get_db)):
    find_blog = db.query(models.Post).filter(models.Post.id == id)
    update_blog = find_blog.first()

    if update_blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Blog not found")
    
    find_blog.update(blog.model_dump(), synchronize_session = False)

    db.commit()

    return find_blog.first()


@app.delete("/blog/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    finded_blog = db.query(models.Post).filter(models.Post.id == id)
    delete_blog = finded_blog.first()

    if delete_blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Blog Not Found")
    finded_blog.delete(synchronize_session= False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)