from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Room, Client, Booking
from datetime import time, datetime
import json

router = APIRouter()

@router.post("/load_initial_data/")
def load_initial_data(db: Session = Depends(get_db)):
    try:
        # Cargar datos iniciales desde un archivo JSON
        with open('initial_data.json', 'r') as file:
            data = json.load(file)

        initial_rooms = data["rooms"]
        initial_clients = data["clients"]
        initial_bookings = data["bookings"]

        for room_data in initial_rooms:
            room_data["opening_hour"] = time.fromisoformat(room_data["opening_hour"])
            room_data["closing_hour"] = time.fromisoformat(room_data["closing_hour"])
            room = Room(**room_data)
            db.add(room)

        for client_data in initial_clients:
            client = Client(**client_data)
            db.add(client)

        db.commit()  # Commit here to ensure rooms and clients are saved before adding bookings

        for booking_data in initial_bookings:
            booking_data["start_time"] = datetime.strptime(booking_data["start_time"], "%H:%M:%S").time()
            booking_data["end_time"] = datetime.strptime(booking_data["end_time"], "%H:%M:%S").time()
            booking = Booking(**booking_data)
            db.add(booking)

        db.commit()
        return {"message": "Initial data loaded successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
