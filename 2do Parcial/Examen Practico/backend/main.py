from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from backend import data_service

app = FastAPI(title="Amazon Books Statistics API")

# Permitir CORS (útil para desarrollo local si frontend y backend corren separados)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/categorical-frequencies")
def get_categorical_frequencies():
    """
    Retorna frecuencias absolutas y relativas (basado en Category)
    """
    return data_service.get_categorical_frequencies()

@app.get("/api/continuous-frequencies")
def get_continuous_frequencies():
    """
    Retorna frecuencias para histogramas y polígonos usando la variable Price.
    """
    return data_service.get_continuous_frequencies(bins=15)

@app.get("/api/statistics")
def get_statistics():
    """
    Retorna Media, Mediana y Moda de las variables numéricas clave.
    """
    return data_service.get_statistics()

@app.get("/api/data")
def get_raw_data():
    """
    Retorna una muestra de los datos crudos para la tabla.
    """
    return data_service.get_raw_data(limit=20)

# Montar el Frontend
# NOTA: Para arquitectura de 'cero monolitos', montamos estáticos aquí
# para facilidad de hosting gratuito (Render), pero el frontend y backend no se mezclan.
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
