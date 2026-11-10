"""
Administración de notas de un curso (versión POO): la clase Estudiante.

Un estudiante guarda juntos su Id, su nombre y su nota. Los atributos son
privados: desde afuera solo se leen con los get_ y la nota solo se cambia
con set_nota, que valida el rango.
"""


class Estudiante:
    NOTA_MINIMA = 0.0
    NOTA_MAXIMA = 5.0

    def __init__(self, id, nombre, nota):
        """
        Supone: id y nombre son textos; nota está entre NOTA_MINIMA y
        NOTA_MAXIMA (el constructor no valida).
        Garantiza: crea un estudiante con esos datos.
        """
        self.__id = id
        self.__nombre = nombre
        self.__nota = nota

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        """
        Garantiza: si nota está entre NOTA_MINIMA y NOTA_MAXIMA, la
        guarda y retorna True. Si no, no cambia nada y retorna False.
        """
        cambiada = False
        if Estudiante.NOTA_MINIMA <= nota <= Estudiante.NOTA_MAXIMA:
            self.__nota = nota
            cambiada = True
        return cambiada

    def __str__(self):
        """Garantiza: retorna 'Id \\t nombre \\t nota', una línea del listado."""
        return (self.__id + " \t " + self.__nombre
                + " \t " + str(self.__nota))
