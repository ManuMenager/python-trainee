# Altas de alumnos y gestión de notas
import persistenciaTXT as pTXT

def agregar_alumno(alumno, alumnos):
    legajo = int(alumno['legajo'])
    if legajo in alumnos:
        print("El alumno ya existe.")
        return False # Se podría utilizar excepciones para hacerlo de una mejor manera.
    
    alumnos[legajo] = alumno
    return True


def agregar_nota_alumno(nota, legajo, alumnos):
    legajo = int(legajo)

    if legajo not in alumnos:
        return False

    alumnos[legajo]["notas"].append(nota)
    return True