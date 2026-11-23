"""
Clase 15 - Modo "w" frente a modo "a".

"w" (write) empieza el archivo desde cero: borra lo que tenia.
"a" (append) agrega al final: conserva lo que tenia.
"""


def mostrar(nombre_archivo):
    """Garantiza: muestra el contenido del archivo entre dos rayas."""
    archivo = open(nombre_archivo, "r")
    print(archivo.read(), end="")
    archivo.close()
    print("-----")


archivo = open("lista.txt", "w")
archivo.write("Juan\n")
archivo.write("Ana\n")
archivo.close()
mostrar("lista.txt")

archivo = open("lista.txt", "a")      # agrega al final
archivo.write("Clara\n")
archivo.write("Julia\n")
archivo.close()
mostrar("lista.txt")

archivo = open("lista.txt", "w")      # empieza de cero: Juan, Ana, Clara y Julia se pierden
archivo.write("Pedro\n")
archivo.close()
mostrar("lista.txt")
