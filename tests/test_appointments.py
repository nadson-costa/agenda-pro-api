from fastapi.testclient import TestClient
from app.main import app
import random
import string

client = TestClient(app)

def test_create_appointment_success():

    prof_suffix = ''.join(random.choices(string.ascii_lowercase, k=6))
    prof_email = f"profissional_{prof_suffix}@teste-automatizado.com"
    prof_payload = {
        "nome": "Profissional Teste",
        "email": prof_email,
        "password": "123",
        "tipo_usuario": "profissional"
        }
    prof_response = client.post("/usuarios", json=prof_payload)
    assert prof_response.status_code == 201, "Falha ao criar usuário do tipo 'profissional'."
    professional_id = prof_response.json()["id"] 

    client_suffix = ''.join(random.choices(string.ascii_lowercase, k=6))
    client_email = f"cliente_{client_suffix}@teste-automatizado.com"
    client_payload = {
        "nome": "Cliente Teste", 
        "email": client_email,
        "password": "123",
        "tipo_usuario": "cliente"
        }
    client_response = client.post("/usuarios", json=client_payload)
    assert client_response.status_code == 201, "Falha ao criar usuário cliente."


    login_data = {"username": client_email, "password": "123"}
    login_response = client.post("/login", data=login_data)
    assert login_response.status_code == 200, f"Falha no login. Body: {login_response.json()}"
    token = login_response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    appointment_payload = {
        "profissional_id": professional_id, 
        "data_hora_inicio": "2025-09-01T10:00:00",
        "data_hora_fim": "2025-09-01T11:00:00",
        "observacoes": "Teste de agendamento"
    }
    response = client.post("/agendamentos", json=appointment_payload, headers=headers)

   
    assert response.status_code == 201, f"Falha ao criar agendamento. Body: {response.json()}"
    assert response.json()["observacoes"] == "Teste de agendamento"
    assert response.json()["profissional_id"] == professional_id