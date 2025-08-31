from datetime import datetime, timedelta, timezone
from jose import JWSError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import session
from . import models, database
from .models import tables


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "teste-api"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Credenciais invalidas",
        headers = {"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        
        #token_data = schemas.TokenData(email = email)
        
    except JWSError:
        raise credentials_exception
    
    user = db.query(models.tables.Usuario).filter(models.tables.Usuario.email == email).first()
    if user is None:
        raise credentials_exception
    
    return user
