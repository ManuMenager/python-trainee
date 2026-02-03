# Persistencia JSON
import json

def cargar_desde_txt(): # Archivo → Diccionario
    try:
        with open("semana1/dia4_persistencia_y_organizacion/alumnos.json", "r", encoding="utf-8") as archivo:
            alumnos = json.load(archivo)

            alumnos = {int(k): v for k, v in alumnos.items()}

    except FileNotFoundError:
        alumnos = {}

    return alumnos

def guardar_en_txt(alumnos): # Diccionario → Archivo
    with open("semana1/dia4_persistencia_y_organizacion/alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump(alumnos, archivo, indent=4, ensure_ascii=False)