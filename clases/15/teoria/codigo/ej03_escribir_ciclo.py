"""
Clase 15 - Escribir varias lineas con un ciclo.

Cada elemento de la lista se escribe en su propia linea. write() solo
recibe texto: un numero se convierte antes con str() o con un f-string.
"""

nombres = ["Ana", "Beto", "Carla", "Dario"]
notas = [3.0, 4.5, 2.0, 4.0]

archivo = open("nombres.txt", "w")
for i in range(len(nombres)):
    archivo.write(nombres[i] + "\n")
archivo.close()

archivo = open("notas.txt", "w")
for i in range(len(notas)):
    archivo.write(f"{notas[i]}\n")    # o: str(notas[i]) + "\n"
    # archivo.write(notas[i])         # da TypeError: no es texto
archivo.close()

archivo = open("notas.txt", "r")
print(archivo.read())
archivo.close()
