# Composición = 'tiene un'
class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)