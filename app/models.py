from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    opening_hour = Column(Time)
    closing_hour = Column(Time)
    capacity = Column(Integer)

    bookings = relationship("Booking", back_populates="room")

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    bookings = relationship("Booking", back_populates="client")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    start_time = Column(Time)
    end_time = Column(Time)

    room = relationship("Room", back_populates="bookings")
    client = relationship("Client", back_populates="bookings")
