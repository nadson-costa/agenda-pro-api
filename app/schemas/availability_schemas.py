from pydantic import BaseModel, ConfigDict
from datetime import time

class AvailabilityCreate(BaseModel):
    dia_semana: int
    horario_inicio: time
    horario_fim: time

class AvailabilityResponse(BaseModel):
    id: int
    profissional_id: int
    dia_semana: int
    horario_inicio: time
    horario_fim: time

    model_config = ConfigDict(from_attributes=True)