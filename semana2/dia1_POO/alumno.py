class Alumno:
    def __init__(self, legajo, nombre):
        self.legajo = legajo
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print("Nota inválida.")
    
    def promedio(self):
        return sum(self.notas) / len(self.notas)