"""
Clase 15 - Un vistazo a try / except (no es tema del curso).

try intenta un bloque; si ocurre el error nombrado en except, en vez de
detenerse el programa ejecuta ese otro bloque. Se ve a fondo en cursos
posteriores (manejo de excepciones).
"""

nombre_archivo = "notas.cvs"
try:
    archivo = open(nombre_archivo, "r")
    print(archivo.read())
    archivo.close()
except FileNotFoundError:
    print("No se encontro el archivo", nombre_archivo)
