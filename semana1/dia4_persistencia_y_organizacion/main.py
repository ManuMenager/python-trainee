# Flujo del programa
import calculos
import alumnos
import persistenciaTXT as pTXT
import persistenciaJSON as pJSON

legajos_alumnos = pTXT.cargar_desde_txt()

alumno1 = {
    "legajo": 1,
    "nombre": "Emanuel",
    "notas": [9,7,9]
}

alumno2 = {
    "legajo": 2,
    "nombre": "Pepito",
    "notas": [9,8]
}

if alumnos.agregar_alumno(alumno1, legajos_alumnos):
    pTXT.guardar_en_txt(legajos_alumnos)

if alumnos.agregar_alumno(alumno2, legajos_alumnos):
    pTXT.guardar_en_txt(legajos_alumnos)

print(f"Alumnos: {legajos_alumnos}")

if alumnos.agregar_nota_alumno(7, alumno2["legajo"], legajos_alumnos):
    pTXT.guardar_en_txt(legajos_alumnos)


print("Notas de Pepito: ", legajos_alumnos[2]["notas"])

print("Promedio de cada alumno:", calculos.promedio_alumnos(legajos_alumnos))

print("Promedio general:", calculos.promedio_general(legajos_alumnos))