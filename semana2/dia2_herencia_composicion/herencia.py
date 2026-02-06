# Herencia = 'es un'
class Persona: # Clase Padre
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Hola, soy {self.nombre}")
    
class Alumno(Persona): # Clase Hijo
    def __init__(self, nombre):
        super().__init__(nombre) # Llama al Constructor de la clase padre (Persona)
        self.notas = []
    
    # Hereda los métodos de la clase Persona: presentarse()
    # Por lo tanto se evita código repetido.

    # Override de métodos
    def presentarse(self):
        print(f"Hola, soy el alumno {self.nombre}")