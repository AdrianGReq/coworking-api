from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import Room, Client, Booking

# Configura la URL de la base de datos
DATABASE_URL = "sqlite:///./test.db"  # Ajusta la URL según tu configuración

# Crea el motor y la sesión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
