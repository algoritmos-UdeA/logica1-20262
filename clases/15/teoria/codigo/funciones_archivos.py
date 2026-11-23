"""
Clase 15 - Funciones que leen y escriben archivos.

Las funciones reciben el NOMBRE del archivo, no el archivo abierto: cada
una lo abre, hace su trabajo y lo cierra. Una funcion retorna una sola
cosa; por eso los nombres y las notas se leen con dos funciones.
Formato del archivo (CSV): un encabezado y una linea por estudiante,
    nombre,parcial1,parcial2,parcial3
"""


def leer_nombres(nombre_archivo):
    """
    Supone:
        nombre_archivo es un CSV con el formato del modulo, que existe en
        la carpeta de trabajo.
    Garantiza:
        Retorna una lista nueva con los nombres, en el orden del archivo.
        No modifica el archivo.
    """
    nombres = []
    archivo = open(nombre_archivo, "r")
    archivo.readline()                       # el encabezado
    for linea in archivo:
        partes = linea.strip().split(",")
        nombres.append(partes[0])
    archivo.close()
    return nombres


def leer_notas(nombre_archivo):
    """
    Supone:
        nombre_archivo es un CSV con el formato del modulo, que existe en
        la carpeta de trabajo.
    Garantiza:
        Retorna una matriz nueva con una fila por estudiante y una columna
        por parcial (float). No modifica el archivo.
    """
    notas = []
    archivo = open(nombre_archivo, "r")
    archivo.readline()                       # el encabezado
    for linea in archivo:
        partes = linea.strip().split(",")
        fila = []
        for j in range(1, len(partes)):
            fila.append(float(partes[j]))
        notas.append(fila)
    archivo.close()
    return notas


def guardar_curso(nombre_archivo, nombres, notas):
    """
    Supone:
        nombres y notas tienen la misma cantidad de filas, y cada fila de
        notas tiene 3 parciales.
    Garantiza:
        CREA el archivo (o lo REEMPLAZA si ya existia) con un encabezado y
        una linea por estudiante. No retorna nada.
    """
    archivo = open(nombre_archivo, "w")
    archivo.write("nombre,parcial1,parcial2,parcial3\n")
    for i in range(len(nombres)):
        archivo.write(f"{nombres[i]},{notas[i][0]},{notas[i][1]},{notas[i][2]}\n")
    archivo.close()
