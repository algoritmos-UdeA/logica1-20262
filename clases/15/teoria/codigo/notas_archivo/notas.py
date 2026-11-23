"""
Clase 15 - Notas finales de un curso, leidas de un archivo: funciones.

El mismo problema de la clase 14 (notas de tres parciales con pesos
30 %, 30 % y 40 %), ahora con los datos en notas.csv y el resultado
guardado en notas_finales.csv. calcular_notas_finales, buscar_mayor y
buscar_menor son las mismas de la clase 14.
"""


def leer_nombres(nombre_archivo):
    """
    Supone:
        nombre_archivo es un CSV (encabezado + nombre,p1,p2,p3) que existe.
    Garantiza:
        Retorna una lista nueva con los nombres, en el orden del archivo.
    """
    nombres = []
    archivo = open(nombre_archivo, "r")
    archivo.readline()
    for linea in archivo:
        partes = linea.strip().split(",")
        nombres.append(partes[0])
    archivo.close()
    return nombres


def leer_notas(nombre_archivo):
    """
    Supone:
        nombre_archivo es un CSV (encabezado + nombre,p1,p2,p3) que existe.
    Garantiza:
        Retorna una matriz nueva: una fila por estudiante, una columna por
        parcial (float).
    """
    notas = []
    archivo = open(nombre_archivo, "r")
    archivo.readline()
    for linea in archivo:
        partes = linea.strip().split(",")
        fila = []
        for j in range(1, len(partes)):
            fila.append(float(partes[j]))
        notas.append(fila)
    archivo.close()
    return notas


def calcular_notas_finales(notas, pesos):
    """
    Supone:
        notas es una matriz de numeros con al menos una fila, y pesos es
        una lista con un peso por columna de notas; los pesos suman 1.0.
    Garantiza:
        Retorna una lista nueva con la nota final de cada fila: la suma
        de notas[i][j] * pesos[j]. No modifica notas ni pesos.
    """
    n = len(notas)
    finales = [0.0] * n
    for i in range(n):
        suma = 0.0
        for j in range(len(pesos)):
            suma = suma + notas[i][j] * pesos[j]
        finales[i] = suma
    return finales


def buscar_mayor(valores):
    """
    Supone:
        valores es una lista de numeros con al menos un elemento.
    Garantiza:
        Retorna el mayor valor de la lista. No modifica valores.
    """
    mayor = valores[0]
    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
    return mayor


def buscar_menor(valores):
    """
    Supone:
        valores es una lista de numeros con al menos un elemento.
    Garantiza:
        Retorna el menor valor de la lista. No modifica valores.
    """
    menor = valores[0]
    for i in range(1, len(valores)):
        if valores[i] < menor:
            menor = valores[i]
    return menor


def guardar_finales(nombre_archivo, nombres, finales):
    """
    Supone:
        nombres y finales tienen el mismo tamano.
    Garantiza:
        CREA el archivo (o lo REEMPLAZA) con el encabezado "nombre,final"
        y una linea por estudiante, con la nota final redondeada a dos
        decimales. No retorna nada.
    """
    archivo = open(nombre_archivo, "w")
    archivo.write("nombre,final\n")
    for i in range(len(nombres)):
        archivo.write(f"{nombres[i]},{finales[i]:.2f}\n")
    archivo.close()
