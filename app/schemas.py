from pydantic import BaseModel, Field
from datetime import time

class RoomCreate(BaseModel):
    name: str
    opening_hour: time = Field(default_factory=lambda: time(hour=0, minute=0, second=0))
    closing_hour: time = Field(default_factory=lambda: time(hour=0, minute=0, second=0))
    capacity: int

class Room(RoomCreate):
    id: int

    class Config:
        from_attributes = True

class ClientCreate(BaseModel):
    name: str

class Client(ClientCreate):
    id: int

    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    room_id: int
    client_id: int
    start_time: time
    end_time: time

class Booking(BookingCreate):
    id: int

    class Config:
        from_attributes = True

class BookingReport(BaseModel):
    client_name: str
    room_name: str
    start_time: time
    end_time: time
    number_of_bookings: int

    class Config:
        from_attributes = True
