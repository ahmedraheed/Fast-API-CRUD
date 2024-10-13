from sqlalchemy.orm import Session
from .. import models, schemas, hashing


def add_new_user(request,db:Session):
    new_user = models.Userblog(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    # new_user=models.Userblog(name=request.name,email=request.email,password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(db:Session):
    blogs = db.query(models.Userblog).all()
    return blogs