"""
Resumen:
Este ejemplo usa un ciclo controlado por un contador. El ciclo se ejecuta un número determinado de veces, que es 
el número de estudiantes al que se le ingresará la nota.
"""

# Constantes
NOTA_MINIMA = 3.0

# Inicializacion
notas_reprobadas = 0
notas_aprobadas = 0
suma_reprobadas = 0
suma_aprobadas = 0
i = 0

# Solicitud de la nota del estudiante
N = int(input('Ingrese el número de estudiantes: '))
while i < N:
    nota = float(input(f'Ingrese la nota del estudiante {i+1}: '))
    # Validadación si gano o perdio
    if nota >= NOTA_MINIMA:
        # Gano
        notas_aprobadas += 1    
        suma_aprobadas += nota  
    else:
        # Perdio
        notas_reprobadas += 1
        suma_reprobadas += nota

    # Solicitud de la nota del estudiante
    i += 1

# Calculo de los totales 
suma_notas = suma_reprobadas + suma_aprobadas
if N == 0:
    # Caso en el que no hay estudiantes
    print("No hay estudiantes")
else:
    # Calculo de los porcentajes y promedios
    p_aprobaron = (notas_aprobadas/N)*100
    p_reprobaron = (notas_reprobadas/N)*100
    prom_nota_reprobada = suma_reprobadas/notas_reprobadas
    prom_nota_aprobada = suma_aprobadas/notas_aprobadas
    prom = suma_notas/N

    # Salida de datos
    print(f"Porcentaje de estudiantes que aprobaron: {p_aprobaron}%")
    print(f"Porcentaje de estudiantes que reprobaron: {p_reprobaron}%")
    print(f"Promedio de notas reprobadas: {prom_nota_reprobada}")
    print(f"Promedio de notas aprobadas: {prom_nota_aprobada}")
    print(f"Promedio general de notas: {prom}")

