from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, models, token
from ..hashing import Hash
from ..schemas import Token

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', response_model=Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    # Fetch user from the database by username
    user = db.query(models.Userblog).filter(models.Userblog.name == request.username).first()

    # If user doesn't exist, raise exception
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')

    # Verify the password
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid password')

    # Create access token
    access_token = token.create_access_token(data={"sub": user.name})
    return {"access_token": access_token, "token_type": "bearer"}

