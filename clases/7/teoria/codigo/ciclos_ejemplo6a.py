"""
Resumen:
Este ejemplo usa una bandera para el control del ciclo. La bandera es una variable que indica si hay o no estudiantes 
a los que se les ingresará la nota. En este caso, la bandera es una variable de tipo string que puede tomar 
los valores 's' (sí) o 'n' (no).
"""

# Constantes
NOTA_MINIMA = 3.0

# Inicializacion
notas_reprobadas = 0
notas_aprobadas = 0
suma_reprobadas = 0
suma_aprobadas = 0

# Inicio del ciclo de lectura de notas (se valida si hay estudiante al que se le ingresará la nota)
hay_estudiante = input('¿Hay estudiante? (s/n): ')
while hay_estudiante == 's':
    # Solicitud de la nota del estudiante
    nota = float(input('Ingrese la nota del estudiante: '))

    # Validadación si gano o perdio
    if nota >= NOTA_MINIMA:
        # Gano
        notas_aprobadas += 1    
        suma_aprobadas += nota  
    else:
        # Perdio
        notas_reprobadas += 1
        suma_reprobadas += nota

    # Se pregunta si hay otro estudiante al que se le ingresará la nota
    hay_estudiante = input('¿Hay estudiante? (s/n): ')

# Calculo de los totales 
num_notas = notas_reprobadas + notas_aprobadas
suma_notas = suma_reprobadas + suma_aprobadas
if num_notas == 0:
    # Caso en el que no hay estudiantes
    print("No hay estudiantes")
else:
    # Calculo de los porcentajes y promedios
    p_aprobaron = (notas_aprobadas/num_notas)*100
    p_reprobaron = (notas_reprobadas/num_notas)*100
    prom_nota_reprobada = suma_reprobadas/notas_reprobadas
    prom_nota_aprobada = suma_aprobadas/notas_aprobadas
    prom = suma_notas/num_notas

    # Salida de datos
    print(f"Porcentaje de estudiantes que aprobaron: {p_aprobaron}%")
    print(f"Porcentaje de estudiantes que reprobaron: {p_reprobaron}%")
    print(f"Promedio de notas reprobadas: {prom_nota_reprobada}")
    print(f"Promedio de notas aprobadas: {prom_nota_aprobada}")
    print(f"Promedio general de notas: {prom}")

