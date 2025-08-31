from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import session
from .. import schemas, models, database
from ..schemas import user_schemas
from ..models import tables
from passlib.context import CryptContext
from .. import hashing
from .. import token as oauth2_token


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

def get_db():
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=user_schemas.UserResponse, status_code=201)
def crate_user(request: user_schemas.UserCreate, db: session = Depends(get_db)):
    hashed_password = hashing.Hash.bcrypt(request.password )

    new_user = models.tables.Usuario(
        nome = request.nome,
        email = request.email,
        senha_hash = hashed_password,
        tipo_usuario = request.tipo_usuario
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/me", response_model=user_schemas.UserResponse)
def get_current_user_details(current_user: models.tables.Usuario = Depends(oauth2_token.get_current_user)):       
    return current_user
