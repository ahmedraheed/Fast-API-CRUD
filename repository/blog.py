from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_by_id(id,db:Session,res,):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=404, detail=f'bolg with this id {id} is not avalible')
        # res.status_code=status.HTTP_404_NOT_FOUND
        # return {'details':f' bolg with this id {id} is not avalible '}
    return blogs


def create(Blog:schemas.Blog,db:Session):
    new_blog = models.Blog(title=Blog.title, body=Blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id, db: Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id,request: schemas.Blog,db:Session):
    update_data = request.model_dump(exclude_unset=True)
    # db.query(models.Blog).filter(models.Blog.id==id).update(update_data)
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'the blog of {id} not found')
    blog.update(update_data)
    db.commit()
    db.refresh(blog)
    return blog