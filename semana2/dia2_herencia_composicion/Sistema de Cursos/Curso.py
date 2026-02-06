class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []
    
    def agregar_alumno(self, alumno):
        if alumno in self.alumnos:
            raise ValueError("El alumno ya pertenece al curso.")
        self.alumnos.append(alumno)
    
    def promedios(self):
        promedios = []
        for alumno in self.alumnos:
            promedios.append(alumno.promedio())
        return promedios