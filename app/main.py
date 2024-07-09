from fastapi import FastAPI
from app.endpoints import rooms, clients, bookings, initial_data_loader, reports

app = FastAPI()

app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
app.include_router(initial_data_loader.router, prefix="/load_data", tags=["load_data"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Coworking API"}
