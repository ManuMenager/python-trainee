# While: No se cuantas veces se va a repetir, pero se que se va a repetir hasta que una condición se cumpla.

# Solicita al usuario que ingrese un número entre 0 y 10 hasta que lo haga correctamente, verificando que la entrada sea válida (es un número entero).
numero = input("Ingresa un número del 0 al 10: ")
while True:
    try:
        numero = int(numero)
        if 0 <= numero <= 10:
            print(f"Número válido: {numero}")
        else:
            print("Número inválido. Intenta de nuevo.")
            numero = input("Ingresa un número del 0 al 10: ")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
        numero = input("Ingresa un número del 0 al 10: ")


# For: Se cuantas veces se va a repetir, ya que recorro una lista o un rango específico.

# Mostrar los números del 1 al 10.
for i in range(1, 11):
    print(i)

# Mostrar solo los pares del 1 al 10.
for i in range(1, 11):
    if i%2 == 0:
        print(i)

# Calcular suma del 1 al 100.
contador = 0
for i in range(1, 101):
    contador += i
print(contador)


# Listas: Colección de elementos ordenados y mutables.
numeros = [5, 10, 3, 8]

x = numeros[0] #Acceder por índice.
numeros.append(15) #Agregar un elemento al final.
numeros.remove(3) #Eliminar un elemento por valor.

numbers = []

for i in range(1,6):
    numero = input("Ingrese un numero: ")
    numbers.append(int(numero))

# Muestra los elementos de la lista
for n in numbers:
    print(n)

# Suma total de los elementos
cont = 0
for n in numbers:
    cont += n
print(cont)

# Promedio (sin usar función len)
cant_elems = 0
for n in numbers:
    cant_elems += 1
print(cont / cant_elems)

# EJERCICIOS

# Contador simple
numero_ingresado = int(input("Ingrese un número: "))
total = 0
cant_ingresados = 0 
while numero_ingresado != 0:
    total += numero_ingresado
    cant_ingresados += 1
    numero_ingresado = int(input("Ingrese un número: "))
print(f"La soma total es: {total} y la cantidad de números es: {cant_ingresados}")

# Registro de notas
nota = int(input("Ingrese una nota: "))
notas = []
while nota != -1:
    notas.append(nota)
    nota = int(input("Ingrese una nota: "))

for n in notas:
    print(n)

total = 0
for n in notas:
    total += n
print(f"El promedio de notas es: {total / len(notas)}")
print(f"La nota mas alta es: {min(notas)}")
print(f"La nota mas baja es: {max(notas)}")