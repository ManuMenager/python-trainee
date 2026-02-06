class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        if not 0 <= nota <= 10:
            raise ValueError("Nota inválida.")

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def agregar_alumno(self, alumno):
        if alumno in self.alumnos:
            raise ValueError("El alumno ya está en el curso.")
        self.alumnos.append(alumno)

alumno = Alumno("Emanuel")
curso = Curso("Python")

# Manejo desde fuera
try:
    alumno.agregar_nota(-5)
except ValueError as e:
    print(e)

try:
    curso.agregar_alumno(alumno)
    print(f"Alumno agregado: {alumno.nombre}")
except ValueError as e:
    print(e)

try:
    curso.agregar_alumno(alumno)
    print(f"Alumno agregado: {alumno.nombre}")
except ValueError as e:
    print(e)