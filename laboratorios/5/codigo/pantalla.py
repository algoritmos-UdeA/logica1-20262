"""
Laboratorio 5 - Parqueadero: lo que se muestra en pantalla.

ESTE ARCHIVO YA ESTÁ COMPLETO. No hay que modificarlo.

Dibuja el mapa del parqueadero, la lista de vehículos y el recibo. No
crea objetos ni cambia nada: solo les pregunta al parqueadero, a sus
puestos, a los vehículos y al recibo, usando sus métodos públicos. Por
eso no importa ningún otro archivo del laboratorio.

Las funciones texto_... RETORNAN el texto (así se pueden probar con
assert) y las funciones mostrar_... lo imprimen.

Métodos de las clases que este archivo usa:
    Parqueadero: get_pisos(), get_puestos_por_piso(), get_puesto(piso, numero),
                 contar_libres()
    Puesto:      esta_libre(), get_vehiculo()
    Vehiculo:    get_placa(), get_tipo()
    Recibo:      get_vehiculo(), get_minutos(), calcular_horas(), calcular_valor()

Los pisos y los puestos se muestran contando desde 1, que es como los ve
el usuario.
"""


def texto_puesto(puesto):
    """
    Supone: puesto es un objeto Puesto.
    Garantiza: retorna "[   ]" si el puesto está libre. Si está ocupado,
    retorna la inicial del tipo de vehículo entre corchetes: "[ C ]" para
    un carro y "[ M ]" para una moto.
    """
    texto = "[   ]"
    if not puesto.esta_libre():
        inicial = puesto.get_vehiculo().get_tipo()[0].upper()
        texto = "[ " + inicial + " ]"
    return texto


def texto_encabezado(puestos_por_piso):
    """
    Supone: 1 <= puestos_por_piso <= 9.
    Garantiza: retorna la línea con el número de cada puesto (1, 2, 3...),
    alineada con los corchetes del mapa.
    """
    texto = "       "
    for numero in range(1, puestos_por_piso + 1):
        if numero > 1:
            texto = texto + " "
        texto = texto + "  " + str(numero) + "  "
    return texto.rstrip()


def texto_piso(parqueadero, piso):
    """
    Supone: parqueadero es un objeto Parqueadero y 1 <= piso <= pisos.
    Garantiza: retorna una línea con todos los puestos de ese piso, por
    ejemplo "Piso 1 [ C ] [   ] [ M ]".
    """
    texto = "Piso " + str(piso)
    for numero in range(1, parqueadero.get_puestos_por_piso() + 1):
        texto = texto + " " + texto_puesto(parqueadero.get_puesto(piso, numero))
    return texto


def texto_mapa(parqueadero):
    """
    Supone: parqueadero es un objeto Parqueadero con máximo 9 pisos y
    máximo 9 puestos por piso.
    Garantiza: retorna el mapa completo: el encabezado, una línea por piso
    (el piso más alto arriba, como en un edificio), la leyenda y cuántos
    puestos libres hay.
    """
    pisos = parqueadero.get_pisos()
    puestos_por_piso = parqueadero.get_puestos_por_piso()
    texto = texto_encabezado(puestos_por_piso) + "\n"
    for piso in range(pisos, 0, -1):
        texto = texto + texto_piso(parqueadero, piso) + "\n"
    texto = texto + "\n"
    texto = texto + "C: carro   M: moto   [   ]: libre\n"
    texto = (texto + "Libres: " + str(parqueadero.contar_libres())
             + " de " + str(pisos * puestos_por_piso))
    return texto


def texto_vehiculos(parqueadero):
    """
    Supone: parqueadero es un objeto Parqueadero.
    Garantiza: retorna una línea por cada vehículo que está en el
    parqueadero, con su placa, su tipo y dónde está. Recorre piso por piso
    y, dentro de cada piso, puesto por puesto. Si no hay ninguno, retorna
    "(no hay vehículos)".
    """
    texto = ""
    for piso in range(1, parqueadero.get_pisos() + 1):
        for numero in range(1, parqueadero.get_puestos_por_piso() + 1):
            puesto = parqueadero.get_puesto(piso, numero)
            if not puesto.esta_libre():
                vehiculo = puesto.get_vehiculo()
                if texto != "":
                    texto = texto + "\n"
                texto = (texto + vehiculo.get_placa() + "  " + vehiculo.get_tipo()
                         + "  piso " + str(piso) + ", puesto " + str(numero))
    if texto == "":
        texto = "(no hay vehículos)"
    return texto


def texto_recibo(recibo):
    """
    Supone: recibo es un objeto Recibo.
    Garantiza: retorna el recibo en cuatro líneas: el vehículo, los
    minutos, las horas que se cobran y el valor.
    """
    vehiculo = recibo.get_vehiculo()
    texto = "--- Recibo ---\n"
    texto = texto + "Vehículo: " + vehiculo.get_placa() + " (" + vehiculo.get_tipo() + ")\n"
    texto = texto + "Tiempo: " + str(recibo.get_minutos()) + " minutos\n"
    texto = texto + "Horas cobradas: " + str(recibo.calcular_horas()) + "\n"
    texto = texto + "Valor: $" + str(recibo.calcular_valor())
    return texto


def mostrar_mapa(parqueadero):
    """Garantiza: imprime el mapa del parqueadero. No retorna nada."""
    print(texto_mapa(parqueadero))


def mostrar_vehiculos(parqueadero):
    """Garantiza: imprime los vehículos del parqueadero. No retorna nada."""
    print(texto_vehiculos(parqueadero))


def mostrar_recibo(recibo):
    """Garantiza: imprime el recibo. No retorna nada."""
    print(texto_recibo(recibo))
