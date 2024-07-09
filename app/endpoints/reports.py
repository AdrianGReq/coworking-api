from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db
from datetime import datetime, time

router = APIRouter()

@router.get("/room_usage_percentage/{room_id}", response_model=float)
def get_room_usage_percentage(room_id: int, db: Session = Depends(get_db)):
    return crud.get_room_usage_percentage(db, room_id=room_id)

@router.get("/number_of_bookings_by_client/")
def get_number_of_bookings_by_client_endpoint(client_id: int, db: Session = Depends(get_db)):
    try:
        count = crud.get_number_of_bookings_by_client(db, client_id)
        return {"client_id": client_id, "number_of_bookings": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/overlapping_bookings/{room_id}")
def get_overlapping_bookings_endpoint(room_id: int, db: Session = Depends(get_db)):
    try:
        overlapping_bookings = crud.get_overlapping_bookings(db, room_id)
        return [
            {
                "booking1": {
                    "id": booking1.id,
                    "start_time": booking1.start_time,
                    "end_time": booking1.end_time,
                    "client_id": booking1.client_id
                },
                "booking2": {
                    "id": booking2.id,
                    "start_time": booking2.start_time,
                    "end_time": booking2.end_time,
                    "client_id": booking2.client_id
                }
            }
            for booking1, booking2 in overlapping_bookings
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/room_availability/{room_id}/{time_check}", response_model=bool)
def is_room_available(room_id: int, time_check: str, db: Session = Depends(get_db)):
    try:
        time_check = datetime.strptime(time_check, "%H:%M:%S").time()
        return crud.is_room_available(db, room_id=room_id, time_check=time_check)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid time format. Use HH:MM:SS")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
