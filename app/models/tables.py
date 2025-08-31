from sqlalchemy import (Column, Integer, String, ForeignKey, DateTime, Time, Enum, Text)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)
    tipo_usuario = Column(Enum('profissional', 'cliente', name = 'tipo_usuario_enum'), nullable=False)

    agendamento_cliente = relationship("Agendamento", foreign_keys="[Agendamento.cliente_id]", back_populates="cliente")
    agendamento_profissional = relationship("Agendamento", foreign_keys="[Agendamento.profissional_id]", back_populates="profissional")
    disponibilidades = relationship("Disponibilidade", back_populates="profissional")


class Disponibilidade(Base):
    __tablename__ = "disponibilidades"

    id = Column(Integer, primary_key=True, index=True)
    profissional_id = Column(Integer, ForeignKey("usuarios.id"))
    dia_semana = Column(Integer)
    horario_inicio = Column(Time)
    horario_fim = Column(Time)

    profissional = relationship("Usuario", back_populates="disponibilidades")

class Agendamento(Base):
    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("usuarios.id"))
    profissional_id = Column(Integer, ForeignKey("usuarios.id"))
    data_hora_inicio = Column(DateTime)
    data_hora_fim = Column(DateTime)
    status = Column(Enum('solicitado', 'confirmado', 'cancelado', 'realizado', 'bloqueado', name='status_agendamento_enum'), default='solicitado')
    observacoes = Column(Text, nullable=True)

    cliente = relationship("Usuario", foreign_keys=[cliente_id], back_populates="agendamento_cliente")
    profissional = relationship("Usuario", foreign_keys=[profissional_id], back_populates="agendamento_profissional")



