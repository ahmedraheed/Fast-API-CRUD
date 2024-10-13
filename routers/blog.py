from fastapi import APIRouter, Depends, status, HTTPException,Response
from sqlalchemy.orm import Session
from blog import schemas, models,oauth2
from blog.database import get_db
from blog.schemas import ShowUser

from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

@router.get('/', response_model=list[schemas.Showblog])
def all(db: Session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_all(db)



@router.post("/", status_code=status.HTTP_201_CREATED,tags=["blog"])
def create(Blog:schemas.Blog, db: Session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.create(Blog, db)


@router.delete("/{id}", response_model=schemas.Showblog)
def destroy(id, db: Session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
  return blog.destroy(id, db)


@router.put("/{id}", response_model=schemas.Showblog)
def update(id, request: schemas.Blog, db: Session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', response_model=schemas.Showblog)
def get_by_id(id, res: Response, db: Session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog.get_by_id(id, db, res)



