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

# EJERCICIOS

# Calculadora Simple
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
operador = input("Ingrese la operación (+, -, *, /): ")

while True:
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operador == '+':
            print(num1 + num2)
            break
        elif operador == '-':
            print(num1 - num2)
            break
        elif operador == '*':
            print(num1 * num2)
            break
        elif operador == '/':
            if num2 != 0:
                print(num1 / num2)
                break
            else:
                print("Error: División por cero no permitida.")
                num2 = input("Ingrese el segundo número: ")
        else:
            print("Operación no válida. Por favor ingrese +, -, * o /.")
            operador = input("Ingrese la operación (+, -, *, /): ")
    except ValueError:
        print("Por favor, ingrese números válidos.")
        num1 = input("Ingrese el primer número: ")
        num2 = input("Ingrese el segundo número: ")

# Login hardcodeado
CORRECT_USER = "admin"
CORRECT_PASSWORD = "admin123"

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

cant_intentos = 0

while cant_intentos < 3:
    if user == CORRECT_USER and password == CORRECT_PASSWORD:
        print("Acceso correcto.")
        break
    elif cant_intentos < 2:
        cant_intentos += 1
        print("Usuario o contraseña incorrectos. Intente de nuevo.")
        user = input("Ingrese su usuario: ")
        password = input("Ingrese su contraseña: ")
    else:
        print("Número máximo de intentos alcanzado. Acceso denegado.")
        break