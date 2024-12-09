from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Cargar el dataset al iniciar la API
try:
    # Cambia 'dataset.csv' al nombre real de tu archivo
    df = pd.read_csv('hotaling_cocktails - Cocktails.csv')
except FileNotFoundError:
    raise RuntimeError("No se encontró el archivo 'hotaling_cocktails - Cocktails.csv'. Asegúrate de que está en la misma carpeta que este script.")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de análisis de datos"}

@app.get("/columns")
def get_columns():
    """Devuelve las columnas del dataset"""
    return {"columns": df.columns.tolist()}

@app.get("/stats/{column}")
def column_stats(column: str):
    """Devuelve estadísticas de una columna específica"""
    if column not in df.columns:
        raise HTTPException(status_code=404, detail="Columna no encontrada")
    stats = df[column].describe().to_dict()
    return {"column": column, "stats": stats}
