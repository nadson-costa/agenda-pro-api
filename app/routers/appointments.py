from fastapi import HTTPException, Depends, status, APIRouter
from sqlalchemy.orm import Session
from .. import database, schemas, token, models
from ..schemas import appointments_schemas
from ..models import tables


router = APIRouter(
    prefix="/agendamentos",
    tags=["Agendamentos"]
)

@router.post("/", response_model=appointments_schemas.AppointmentResponse, status_code=201)
def create_appointment(
    request: appointments_schemas.AppointmentCreate,
    db: Session = Depends(database.get_db),
    current_user: tables.Usuario = Depends(token.get_current_user)
):
    
    if current_user.tipo_usuario != 'cliente':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Somente Clientes possuem permissão de fazer agendamentos")
    
    # adicionar lógica para verificar se o horário está livre ou não

    new_appointment = tables.Agendamento(
        profissional_id = request.profissional_id,
        data_hora_inicio = request.data_hora_inicio,
        data_hora_fim = request.data_hora_fim,
        observacoes = request.observacoes,
        cliente_id = current_user.id,
        status = "solicitado"
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment