"""
Resumen:

"""

# Constantes
NOTA_MINIMA = 3.0

# Inicializacion
notas_reprobadas = 0
notas_aprobadas = 0
suma_reprobadas = 0
suma_aprobadas = 0

########################################### Funciones ###########################################

# Definición de funciones

# Función que determina si la nota es aprobatoria
def es_nota_aprobatoria(nota, nota_minima):      
  aprob = nota >= nota_minima
  return aprob

# Función que calcula el promedio de notas
def calcular_promedio(suma, cantidad):   
  if cantidad == 0:        
    prom = 0
  else: 
    prom = suma/cantidad
  return prom

# Función que imprime el reporte de resultados
def imprimir_reporte(est_aprob, est_reprob, suma_aprob, suma_reprob):
    total = est_aprob + est_reprob
    prom_aprob = calcular_promedio(suma_aprob, est_aprob)
    prom_reprob = calcular_promedio(suma_reprob, est_reprob)
    prom_curso = calcular_promedio(suma_aprob + suma_reprob, total)

    print(f"Aprobaron: {est_aprob} ({est_aprob / total * 100:.1f} %)")
    print(f"Reprobaron: {est_reprob} ({est_reprob / total * 100:.1f} %)")
    print(f"Prom aprob: {prom_aprob:.2f}")
    print(f"Prom reprob: {prom_reprob:.2f}")
    print(f"Prom nota: {prom_curso:.2f}")


########################################### Programa Principal ###########################################

# Solicitud de la nota del estudiante
N = int(input('Ingrese el número de estudiantes: '))
for i in range(N):
    # Solicitud de la nota del estudiante
    nota = float(input(f'Ingrese la nota del estudiante {i+1}: '))

    # Validadación si gano o perdio
    aprob = es_nota_aprobatoria(nota, NOTA_MINIMA)
    if aprob:
        # Gano
        notas_aprobadas += 1    
        suma_aprobadas += nota  
    else:
        # Perdio
        notas_reprobadas += 1
        suma_reprobadas += nota

    
if N <= 0:
    # Caso en el que no hay estudiantes
    print("No hay estudiantes")
else:
    # Caso en el que hay estudiantes
    imprimir_reporte(notas_aprobadas, notas_reprobadas, suma_aprobadas, suma_reprobadas)

    
