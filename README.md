Semana 1: Fundamentos de Python
- Variables, condicionales
- Bucles
- Estructuras de Datos (listas, diccionarios, sets)
- Funciones
- Módulos
- Archivos
- Manejo de Errores
- Persistencia de Datos(txt y JSON)

Dia 1: Repaso de tipos, errores, condicionales, etc.
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
    Desafios: 
    - En un primer momento quería iterar en la funcion 'promedio_alumnos()' sobre directamente los alumnos pero no me habia dado cuenta que esto iba a iterar sobre las claves del diccionario 'alumnos' por lo que me dió un error y me di cuenta que era necesario iterar sobre los valores de dicho diccionario(sobre los diccionarios 'alumno').

Dia 4: Organización de Archivos y Persistencia de Datos.
- Organización de funciones por archivo(Flujo del programa, calculos, etc)
- Persistencia de datos utilizando un TXT para poder cerrar el programa y que los datos se mantengan.
- Persistencia de datos utlizando JSON (más legible, automatico, robusto y sin parsing que txt).

    Ejercicios.
- Sistema Simple de Alumnos 2: Mejoré el Sistema del dia 3, utilizando primero archivos txt para guardar los datos y organizando las funciones en archivos según su propósito. Luego utilicé JSON en vez de txt ya que es mucho mejor pero para aprender TXT era interesante.
    Desafios:
    - Nunca habia hecho persistencia de datos con archivos txt por lo que realizar el parsing fue un desafio.
    - En un principio creí que lo mejor era cargar y guardar los datos almacenados dentro de las funciones de los alumnos. Pero luego leí que lo mejor era hacerlo en directamente desde el main, ya que las funciones de negocio no deben saber donde se guardan los datos, por lo que es mejor separar las responsabilidades del programa en capas: persistencia, lógica de negocio, control(main).


Semana 2: Programación Orientada a Objetos
- Clases y Objetos
- __init_ (Constructor)
- Métodos
- Encapsulamiento
- Herencia y Composición
- Try/Except aplicado a clases
- Archivos con POO

Dia 1: Clases, Objetos y Encapsulamiento.
- ¿Qué es una clase?
    Es un molde/esqueleto que define la estructura de como serán los objetos, es decir que métodos, atributos tendrán y el comportamiento.
- ¿Qué es un Objeto?
    Es una instancia concreta de una clase, con valores especificos de dicha clase.
- ¿Qué problema resuelva la POO?
Uno de los principales problemas que resuelve es el "código espagueti", la falta de reutilización y la dificultad para modelar el mundo real. Se agrupan los datos y las funciones que los manipulan dentro una misma "capsula" (Objeto). A parece la Herencia para evitar el código repetido y que muchas clases hereden comportamiento por lo que no es necesario volver a escribir código utilizado por muchas clases. Por último la POO permite programar pensando en "cosas"/"Objetos" que interactúan entre sí, lo cual es mucho más intuituvo y sencillo de diseñar.
    
    Ejercicios.
- Sistema Simple POO: Una clase Alumno, la cual se pueda instanciar a partir de un legajo y nombre, que permite agregar notas a dichos alumnos y consultar su promedio. Como parte del ejercicio el encapsulamiento de la clase Alumno decide si agregar o no la nota dada, a partir de si dicha nota es válida o no.

Dia 2: Herencia, Composición y Errores.
- Repaso de Herencia y Composicion / 'Es un' y 'Tiene un'. Se evita mucho código repetido.
- Manejo de errores donde la clases validan los errores por dentro (clase) y el programa lo maneja desde fuera (main)