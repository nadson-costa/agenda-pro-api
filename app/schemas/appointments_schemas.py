from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class AppointmentCreate(BaseModel):
    profissional_id: int
    data_hora_inicio: datetime
    data_hora_fim: datetime
    observacoes: Optional[str] = None

class AppointmentResponse(BaseModel):
    id: int
    cliente_id: int
    profissional_id: int
    data_hora_inicio: datetime
    data_hora_fim: datetime
    status: str
    observacoes: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


    
