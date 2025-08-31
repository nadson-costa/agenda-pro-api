from fastapi import HTTPException, Depends, status, APIRouter
from sqlalchemy.orm import Session
from datetime import date, time, datetime, timedelta
from .. import database, token
from ..schemas import availability_schemas
from ..models import tables
from typing import List

router = APIRouter(
    prefix="/profissionais",
    tags=["Profissionais"]
)

@router.get("/{profissional_id}/horarios-livres", response_model= List[time])
def get_available_slots(
    profissional_id: int,
    data: date,
    db: Session = Depends(database.get_db),
    ):

    dia_semana = data.isoweekday()

    disponibilidade_padrao = db.query(tables.Disponibilidade).filter(
        tables.Disponibilidade.profissional_id == profissional_id,
        tables.Disponibilidade.dia_semana == dia_semana
    ).first()

    if not disponibilidade_padrao:
        return []
    
    agendamentos_marcados = db.query(tables.Agendamento).filter(
        tables.Agendamento.profissional_id == profissional_id,
        tables.Agendamento.data_hora_inicio >= datetime.combine(data, time.min),
        tables.Agendamento.data_hora_fim <= datetime.combine(data, time.max),
        tables.Agendamento.status.in_(['confirmado', 'bloqueado'])
    ).all()

    horarios_disponiveis = []

    intervalo = timedelta(hours=1)

    slot_atual = datetime.combine(data, disponibilidade_padrao.horario_inicio)
    fim_expediente = datetime.combine(data, disponibilidade_padrao.horario_fim)

    while slot_atual < fim_expediente:
        conflito = False
        for agendamento in agendamentos_marcados:
            if slot_atual < agendamento.data_hora_fim and slot_atual + intervalo > agendamento.data_hora_inicio:
                conflito = True
                break

        if not conflito:
            horarios_disponiveis.append(slot_atual.time())

        slot_atual += intervalo

    return horarios_disponiveis


