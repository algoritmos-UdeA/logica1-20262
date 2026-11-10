"""
Piedra, papel o tijera (versión estructurada): funciones de la partida.

Los datos de la partida viven en main.py, en variables sueltas: el nombre
y los puntos del usuario, y el nombre y los puntos de la máquina. Cada
función recibe los datos que necesita como parámetros.
"""
from reglas import EMPATE, GANA_USUARIO, nombre_jugada


def sumar_si_gana(puntos, resultado, resultado_que_suma):
    """
    Supone: puntos >= 0; resultado es EMPATE, GANA_USUARIO o GANA_MAQUINA.
    Garantiza: retorna puntos + 1 si resultado es resultado_que_suma, y
    puntos si no.
    """
    if resultado == resultado_que_suma:
        puntos = puntos + 1
    return puntos


def partida_terminada(puntos_usuario, puntos_maquina, rondas_para_ganar):
    """
    Garantiza: retorna True si alguno de los dos ya ganó rondas_para_ganar
    rondas, y False si no.
    """
    return (puntos_usuario == rondas_para_ganar
            or puntos_maquina == rondas_para_ganar)


def nombre_ganador(nombre_usuario, puntos_usuario, nombre_maquina, puntos_maquina):
    """
    Supone: la partida terminó (los puntos no son iguales).
    Garantiza: retorna el nombre de quien tiene más puntos.
    """
    if puntos_usuario > puntos_maquina:
        nombre = nombre_usuario
    else:
        nombre = nombre_maquina
    return nombre


def texto_ronda(nombre_usuario, jugada_usuario, nombre_maquina, jugada_maquina, resultado):
    """
    Supone: las jugadas son válidas y resultado es el que les corresponde.
    Garantiza: retorna una línea que describe la ronda, por ejemplo
    "Ana: piedra | Máquina: tijera | gana Ana".
    """
    texto = (nombre_usuario + ": " + nombre_jugada(jugada_usuario) + " | "
             + nombre_maquina + ": " + nombre_jugada(jugada_maquina) + " | ")
    if resultado == EMPATE:
        texto = texto + "empate"
    elif resultado == GANA_USUARIO:
        texto = texto + "gana " + nombre_usuario
    else:
        texto = texto + "gana " + nombre_maquina
    return texto


def texto_marcador(nombre_usuario, puntos_usuario, nombre_maquina, puntos_maquina):
    """Garantiza: retorna el marcador, por ejemplo "Ana 2 - 1 Máquina"."""
    return (nombre_usuario + " " + str(puntos_usuario) + " - "
            + str(puntos_maquina) + " " + nombre_maquina)
