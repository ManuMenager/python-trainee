import Persona as p

class Alumno(p.Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.notas = []
    
    def agregar_nota(self, nota):
        if not 0 <= nota <= 10:
            raise ValueError("Nota inválida.")
        self.notas.append(nota)
    
    def promedio(self):
        return sum(self.notas) / len(self.notas)