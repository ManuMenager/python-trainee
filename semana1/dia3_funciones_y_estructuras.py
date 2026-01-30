# Funciones: Reutilizar lógica, mejorar legibilidad y testear más fácil.

# Función con manejo de errores de entrada.
def pedir_numero():
    while True:
        try:
            numero = int(input("Ingresa un número: "))
            return numero
        except ValueError:
            print("Número inválido. Por favor ingrese un número entero válido.")

def calcular_promedio(lista):
    if not lista:
        return 0
    else:
        return (sum(lista) / len(lista))

# Diccionarios: guarda pares clave-valor. Cada dato tiene un significado por lo que no se depende de índices sino de claves.

alumno = {
    "nombre": "Emanuel",
    "edad": 22,
    "notas": [10,8,8,9,9]
}

print(calcular_promedio(alumno['notas']))

def obtener_datos_alumno(alumno):
    return f""" 
    === DATOS DEL ALUMNO === 
    Nombre: {alumno['nombre']}
    Edad: {alumno['edad']}
    Notas: {alumno['notas']}
    """

print(obtener_datos_alumno(alumno))

# Sets: Colecciones de elementos únicos, sin orden específico. Se utiliza para eliminar duplicados o realizar operaciones matemáticas como intersección, unión y diferencia de conjuntos.

lenguajes = set()
for _ in range(5):
    lenguaje = input("Ingrese un lenguaje: ")
    lenguajes.add(lenguaje)

print(f"Cantidad de lenguajes distintos: {len(lenguajes)}")

# EJERCICIOS

# Sistema Simple de Alumnos
alumnos = {}

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

def agregar_alumno(alumno):
    alumnos[alumno["legajo"]] = alumno

agregar_alumno(alumno1)
agregar_alumno(alumno2)

print(f"Alumnos: {alumnos}")

def agregar_nota_alumno(nota, alumno):
    alumnos[alumno["legajo"]]["notas"].append(nota)

agregar_nota_alumno(7, alumno2)

print("Notas de Pepito: ", alumnos[2]["notas"])

def promedio_alumnos(alumnos):
    promedios = []
    for alumno in alumnos.values():
        promedios.append(calcular_promedio(alumno["notas"]))
    return promedios

print(promedio_alumnos(alumnos))

def promedio_general(alumnos):
    return calcular_promedio(promedio_alumnos(alumnos))

print("Promedio general:", promedio_general(alumnos))