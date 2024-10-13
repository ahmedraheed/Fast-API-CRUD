from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog import schemas, hashing, models, oauth2
from blog.database import get_db
from ..repository import user
from blog.schemas import ShowUser

router = APIRouter(
    prefix="/user",
    tags=["User"])

@router.post('/',response_model=ShowUser)
def user_add(request:schemas.User, db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return user.add_new_user(request,db)

@router.get('/', response_model=list[ShowUser])
def all_user(db: Session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return user.get_all_user(db)
