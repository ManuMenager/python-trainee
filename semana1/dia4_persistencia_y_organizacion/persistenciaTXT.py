# Persistencia TXT (Para entender el concepto nomás)
# "r" → leer
# "w" → escribir (sobreescribe)
# join → lista → string
# split → string → lista
# strip → limpiar basura invisible

def cargar_desde_txt(): # Archivo → Diccionario
    alumnos = {}

    try:
        with open("semana1/dia4_persistencia_y_organizacion/alumnos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()

                if not linea:
                    continue

                legajo_str, nombre, notas_str = linea.split(";")
                legajo = int(legajo_str)

                if notas_str:
                    notas = [int(n) for n in notas_str.split(",")]
                else:
                    notas = []

                alumnos[legajo] = {
                    "legajo": legajo,
                    "nombre": nombre,
                    "notas": notas
                }

    except FileNotFoundError:
        pass  # El archivo no existe todavía → diccionario vacío

    return alumnos

def guardar_en_txt(alumnos): # Diccionario → Archivo
    with open("semana1/dia4_persistencia_y_organizacion/alumnos.txt", "w", encoding="utf-8") as archivo:
        for legajo, alumno in alumnos.items():
            notas = ",".join(str(nota) for nota in alumno["notas"])
            linea = f"{legajo};{alumno['nombre']};{notas}\n"
            archivo.write(linea)