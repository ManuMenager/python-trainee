Dia 1: Fundamentos de Python
- Repaso de tipos de datos, input, print, manejo de errores y condicionales.
- Recordé que el uso de try/except es muy importante cuando es necesario castear un input.

    Ejercicios.
- Calculadora Simple: Utilicé inputs que tomen los números y operador, condicionales para determinar que operación hacer y el try/except para manejar errores, ya sea una división por cero o un número u operador mal ingresado
- Login Hardcodeado: Utilicé variables constantes para recordar el usuario y contraseña correctos. un while para limitar la cantidad de intentos y condicionales para verificar los datos ingresados.

Dia 2: Bucles y Listas
- Repaso de while, for y listas.
- Apliqué el uso de acumuladores.

    Ejercicios.
- Contador Simple: Utilicé dos acumuladores para el total y la cantidad de números ingresados, luego el while en el que mientras no se ingrese el número 0, se puede seguir ingresando números.
- Registro de Notas: En este caso utilicé una lista para guardar las notas ingresadas y un for para calcular la suma total y otro para imprimir todos los números de la lista.
- No utilicé el manejo de errores en el input debido a que queria focalizarme en las listas y bucles.

Dia 3: Funciones y Estructuras de Datos.
- Repaso de cuando y por qué utilizar funciones y para qué sirve utilizar algunas estructuras de datos como el diccionario y el set.

    Ejercicios.
- Sistema Simple de Alumnos: Utilicé un diccionario para guardar a los alumnos (diccionario de diccionario), debido a que queria que los alumnos se puedan buscar con una clave para acceder facilmente a sus datos.
    Problema encontrado y solucionado: En un primer momento quería iterar en la funcion 'promedio_alumnos()' sobre directamente los alumnos pero no me habia dado cuenta que esto iba a iterar sobre las claves del diccionario 'alumnos' por lo que me dió un error y me di cuenta que era necesario iterar sobre los valores de dicho diccionario(sobre los diccionarios 'alumno').