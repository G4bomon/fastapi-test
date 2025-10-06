from fastapi import FastAPI
from routes1 import router as router1  # Importa el router
from routes2 import router as router2  # Importa el router
from routes3 import router as router3  # Importa el router

app = FastAPI()

# Incluye las rutas del router
app.include_router(router1)
app.include_router(router2)
app.include_router(router3)