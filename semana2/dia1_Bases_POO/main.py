import persona as p
import alumno as a

p1 = p.Persona("Emanuel", 22)
p2 = p.Persona("Pepito", 30)

p1.presentarse()

a1 = a.Alumno(1, "Emanuel")
a1.agregar_nota(-10)
a1.agregar_nota(8)
a1.agregar_nota(9)

print(a1.promedio())