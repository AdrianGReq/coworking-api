from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db
from datetime import time

router = APIRouter()

@router.get("/", response_model=list[schemas.Booking])
def read_bookings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return bookings

@router.post("/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)

@router.get("/client/{client_id}", response_model=list[schemas.Booking])
def get_bookings_by_client(client_id: int, db: Session = Depends(get_db)):
    bookings = crud.get_bookings_by_client(db, client_id=client_id)
    return bookings

@router.get("/room/{room_id}", response_model=list[schemas.Booking])
def get_bookings_by_room(room_id: int, db: Session = Depends(get_db)):
    bookings = crud.get_bookings_by_room(db, room_id=room_id)
    return bookings

@router.get("/room_availability/{room_id}/{time_check}", response_model=bool)
def is_room_available(room_id: int, time_check: str, db: Session = Depends(get_db)):
    time_check = datetime.strptime(time_check, "%H:%M:%S").time()
    return crud.is_room_available(db, room_id=room_id, time_check=time_check)
