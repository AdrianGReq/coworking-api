from datetime import time
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from sqlalchemy import func, extract
from app.models import Booking

def get_number_of_bookings_by_client(db: Session, client_id: int):
    return db.query(Booking).filter(Booking.client_id == client_id).count()

def is_room_available(db: Session, room_id: int, time_check: time):
    overlapping_bookings = db.query(Booking).filter(
        Booking.room_id == room_id,
        Booking.start_time <= time_check,
        Booking.end_time >= time_check
    ).all()
    return len(overlapping_bookings) == 0

def get_overlapping_bookings(db: Session, room_id: int):
    overlapping_bookings = db.query(Booking).filter(
        Booking.room_id == room_id
    ).filter(
        or_(
            and_(
                Booking.start_time < Booking2.end_time,
                Booking.end_time > Booking2.start_time,
                Booking.id != Booking2.id
            )
            for Booking2 in db.query(Booking).filter(Booking.room_id == room_id)
        )
    ).all()
    return overlapping_bookings



def get_room_usage_percentage(db: Session, room_id: int):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    total_seconds = db.query(func.sum(extract('epoch', Booking.end_time) - extract('epoch', Booking.start_time))).filter(Booking.room_id == room_id).scalar()
    if total_seconds is None:
        total_seconds = 0

    opening_hour = datetime.combine(datetime.today(), room.opening_hour)
    closing_hour = datetime.combine(datetime.today(), room.closing_hour)
    total_available_hours = (closing_hour - opening_hour).seconds / 3600
    
    usage_percentage = (total_seconds / 3600 / total_available_hours) * 100
    return usage_percentage
