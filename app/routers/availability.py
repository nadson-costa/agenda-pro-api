from fastapi import HTTPException, Depends, status, APIRouter
from sqlalchemy.orm import Session
from .. import database, schemas, token, models
from ..schemas import availability_schemas
from ..models import tables

router = APIRouter(
    prefix="/disponibilidade",
    tags=["Disponibilidade"]
)

@router.post("/", response_model=availability_schemas.AvailabilityResponse, status_code=201)
def create_availability(
    request:availability_schemas.AvailabilityCreate,
    db: Session = Depends(database.get_db),
    current_user: tables.Usuario = Depends(token.get_current_user)
    ):

    if current_user.tipo_usuario != "profissional":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Permissões insuficientes")
    
    new_availability = tables.Disponibilidade(
        dia_semana = request.dia_semana,
        horario_inicio = request.horario_inicio,
        horario_fim = request.horario_fim,
        profissional_id = current_user.id
    )

    db.add(new_availability)
    db.commit()
    db.refresh(new_availability)

    return new_availability