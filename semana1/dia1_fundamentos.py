# Tipos, Manejo de errores y conversión.

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

while True:
    try:
        edad = int(edad)
        break
    except ValueError:
        print("Por favor, ingrese un número válido para la edad.")
        edad = input("Ingrese su edad: ")

print(f"Hola {nombre}, el año que viene vas a tener {edad+1} años.")

# Condicionales con manejo de errores
nota = input("Ingrese su nota: ")

while True:
    try:
        nota = float(nota)
        if 0 <= nota <= 10:
            break
        else:
            print("La nota debe estar entre 0 y 10.")
            nota = input("Ingrese su nota (0-10): ")
    except ValueError:
        print("Por favor, ingrese un número válido para la nota.")
        nota = input("Ingrese su nota (0-10): ")

if nota >= 7:
    print("¡Promocionado!")
elif 4 <= nota < 7:
    print("¡Aprobado!")
else:
    print("¡Desaprobado!")