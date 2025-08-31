from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    password: str
    tipo_usuario: str

class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    tipo_usuario: str

    model_config = ConfigDict(from_attributes=True)