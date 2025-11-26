from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="iesazarquiel")

datos = pd.read_csv("datos_alumnos.csv", encoding="latin1", sep=";")

ids_disponibles = datos["ID"].tolist()

campos_notas = list(datos.columns.difference(["ID", "Nombre", "Apellidos", "Asistencia"]))

@app.get("/info-alumnos")
def obtener_info():
    lista = []

    for _, fila in datos.iterrows():
        nombre = fila["Nombre"]
        id_ = fila["ID"]
        lista.append(f"{nombre} - {id_}")

    return {"alumnos": lista}



@app.get("/asistencia")
def consultar_asistencia(id: int | None = None):
    if id is None:
        return {
            "uso": "Este endpoint admite un parámetro opcional 'id'",
            "ejemplo": "/asistencia?id=1001",
            "ids_disponibles": ids_disponibles
        }

    alumno = datos[datos["ID"] == id]

    if alumno.empty:
        return {"error": "No existe ningún alumno con ese ID"}

    return {
        "id": id,
        "nombre": alumno.iloc[0]["Nombre"],
        "apellidos": alumno.iloc[0]["Apellidos"],
        "asistencia": alumno.iloc[0]["Asistencia"]
    }


@app.get("/notas")
def consultar_notas(id: int | None = None, nota: str | None = None):
    if id is None or nota is None:
        return {
            "uso": "Este endpoint admite dos parámetros: 'id' y 'nota'",
            "ejemplo": "/notas?id=1001&nota=Parcial1",
            "ids_disponibles": ids_disponibles,
            "categorias_notas": campos_notas
        }

    alumno = datos[datos["ID"] == id]

    if alumno.empty:
        return {"error": "ID no encontrado"}

    if nota not in campos_notas:
        return {"error": "Categoría de nota incorrecta"}

    return {
        "id": id,
        "nombre": alumno.iloc[0]["Nombre"],
        "apellidos": alumno.iloc[0]["Apellidos"],
        "nota": nota,
        "calificacion": alumno.iloc[0][nota]
    }
