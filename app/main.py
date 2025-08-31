from fastapi import FastAPI
from .models import tables
from .database import engine
from .routers import users, auth, availability, professionals, appointments

tables.Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(availability.router)
app.include_router(professionals.router)
app.include_router(appointments.router)




@app.get("/")
def read_root():
    return{'status': "API Teste"}