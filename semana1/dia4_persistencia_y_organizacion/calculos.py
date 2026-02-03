# Calculos de promedios
def calcular_promedio(lista):
    if not lista:
        return 0
    else:
        return (sum(lista) / len(lista))
    
def promedio_alumnos(alumnos):
    promedios = []
    for alumno in alumnos.values():
        promedios.append(calcular_promedio(alumno["notas"]))
    return promedios

def promedio_general(alumnos):
    return calcular_promedio(promedio_alumnos(alumnos))