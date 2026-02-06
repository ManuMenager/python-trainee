import Alumno as a
import Curso as c

curso = c.Curso("Python")
alumno = a.Alumno("Emanuel")

try:
    curso.agregar_alumno(alumno)
except ValueError as e:
    print(e)

try:
    curso.agregar_alumno(alumno)
except ValueError as e:
    print(e)

try:
    alumno.agregar_nota(9)
except ValueError as e:
    print(e)

try:
    alumno.agregar_nota(-9)
except ValueError as e:
    print(e)

print(alumno.promedio())

alumno2 = a.Alumno("Pepito")

try:
    curso.agregar_alumno(alumno2)
except ValueError as e:
    print(e)

try:
    alumno2.agregar_nota(8)
except ValueError as e:
    print(e)

print(curso.promedios())