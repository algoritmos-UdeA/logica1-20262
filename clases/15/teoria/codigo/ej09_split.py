"""
Clase 15 - Del texto al dato: strip(), split() y float().

Todo lo que se lee de un archivo es TEXTO. Una linea con varios datos se
parte con split(","), que retorna una lista de textos; cada numero se
convierte con float() o int().
"""

linea = "Beto,4.5,4.0,5.0\n"      # asi llega del archivo

limpia = linea.strip()             # sin el "\n"
partes = limpia.split(",")         # lista de 4 textos
print(partes)

nombre = partes[0]
notas = [float(partes[1]), float(partes[2]), float(partes[3])]
print(nombre, notas)
print(partes[1] + partes[2])       # une textos: no suma
print(notas[0] + notas[1])         # suma numeros
