Prueba técnica Backend, Baobab soluciones
Candidato y autor: Adrian García Requena

Coworking API
Esta es una API REST para gestionar las reservas de salas de reuniones en una empresa de coworking.


# Descripción de la implementación
He utilizado FastAPI para desarrollar una API REST rápida y eficiente, junto con SQLAlchemy para manejar la ORM y SQLite como motor de base de datos por su simplicidad y facilidad de uso. La estructura del proyecto está organizada en varios módulos para mantener el código limpio y escalable.

Tecnologías y Herramientas utilizadas:
FastAPI: Framework moderno y rápido para construir APIs con Python basado en estándares tipo OpenAPI y JSON Schema.
SQLAlchemy: ORM de Python que proporciona un conjunto completo de herramientas para trabajar con bases de datos relacionales.
SQLite: Base de datos liviana y autocompatible ideal para proyectos pequeños y medianos.
Uvicorn: Servidor ASGI ultrarrápido para ejecutar aplicaciones FastAPI.
Pydantic: Librería para la validación de datos basada en Python y utilizada por FastAPI para definir modelos de datos.
Swagger UI: Herramienta para la documentación y prueba interactiva de la API, accesible en /docs.


# Instrucciones para levantar el servicio


1.Clona el repositorio:

Desde github:
git clone https://github.com/AdrianGReq/coworking-api.git

Desde Bundle:
git clone Adriangarciarequenacoworkingapi.bundle coworking-api

cd coworking-api


2.Crea un entorno virtual e instala las dependencias:

python -m venv env
source env/bin/activate  # En Linux o macOS
.\env\Scripts\activate   # En Windows
pip install -r requirements.txt


3.Inicia el servidor:

uvicorn app.main:app --reload

Esto iniciará FastAPI en http://127.0.0.1:8000/ por defecto. Puedes acceder a la documentación interactiva de Swagger UI en http://127.0.0.1:8000/docs.


# Listado de rutas y formato de peticiones/respuestas

1. Listado de salas existentes
Método: GET /rooms/

curl -X GET "http://127.0.0.1:8000/rooms/"


2. Listado de reservas existentes
Método: GET /bookings/

curl -X GET "http://127.0.0.1:8000/bookings/"


3. Crear una reserva indicando sala, cliente, hora de inicio y hora de fin
Método: POST /bookings/

curl -X POST "http://127.0.0.1:8000/bookings/" -H "Content-Type: application/json" -d '{
    "room_id": 7,
    "client_id": 19,
    "start_time": "14:00:00",
    "end_time": "15:00:00"
}'


4. Listado de reservas realizadas por el usuario indicado
Método: GET /bookings/client/{client_id}

curl -X GET "http://127.0.0.1:8000/bookings/client/19"


5. Listado de reservas de una sala indicada
Método: GET /bookings/room/{room_id}

curl -X GET "http://127.0.0.1:8000/bookings/room/7"


6. Dar de alta una nueva sala con todos los datos necesarios
Método: POST /rooms/

curl -X POST "http://127.0.0.1:8000/rooms/" -H "Content-Type: application/json" -d '{
    "name": "New Room",
    "opening_hour": "08:00:00",
    "closing_hour": "18:00:00",
    "capacity": 15
}'


7. Obtener % de uso de las salas
Método: GET /reports/room_usage_percentage/{room_id}

curl -X GET "http://127.0.0.1:8000/reports/room_usage_percentage/7"


8. Obtener el número de reservas realizadas por cada cliente
Método: GET /reports/number_of_bookings_by_client/?client_id={client_id}

curl -X GET "http://127.0.0.1:8000/reports/number_of_bookings_by_client/?client_id=7"


9. Obtener si una sala indicada en un momento determinado estaba libre u ocupada
Método: GET /reports/room_availability/{room_id}/{time_check}

curl -X GET "http://127.0.0.1:8000/reports/room_availability/7/19:30:00"


10. Obtener un listado de las reservas que se han solapado en la misma sala
Método: GET /reports/overlapping_bookings/{room_id}

curl -X GET "http://127.0.0.1:8000/reports/overlapping_bookings/7"


11. Cargar los datos iniciales
Método: POST /load_initial_data/

curl -X POST "http://127.0.0.1:8000/load_initial_data/"


# Conclusiones
La implementación de esta API demuestra el poder y la eficiencia de FastAPI para construir servicios web rápidos y robustos. SQLAlchemy, combinado con SQLite, proporciona una solución ligera y fácil de manejar para la gestión de datos. El uso de Swagger UI a través de FastAPI ofrece una forma intuitiva de interactuar y probar la API, facilitando tanto el desarrollo como el mantenimiento de la misma.

Con esta estructura, la aplicación está bien preparada para escalar y adaptarse a futuros requerimientos, asegurando una base sólida para el desarrollo de nuevas funcionalidades.


Si tienen alguna pregunta o sugerencia, no duden en contactarme.

¡Gracias por esta oportunidad!

Adrian García Requena
