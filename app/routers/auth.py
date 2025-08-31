from fastapi import HTTPException, APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas
from ..hashing import Hash
from .. import token
from ..models import tables

router = APIRouter(
    prefix="/login",
    tags=["Autenticação"]
)

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(tables.Usuario).filter(tables.Usuario.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuário não encontrado ou credenciais inválidas")
    
    if not Hash.verify(user.senha_hash, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Senha incorreta")
    
    access_token = token.create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
