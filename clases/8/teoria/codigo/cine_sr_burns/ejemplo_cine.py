"""
Constantes
"""

# Opciones del menu
VIP = 1
NORMAL = 2
SALIR = 3

# Precios 
VALOR_VIP = 7000
VALOR_NORMAL = 5000
  
# Capacidad del cine
PUESTOS_VIP = 2
PUESTOS_NORMAL = 4
  
"""
Variables
"""

# Contadores
p_VIP_ocupados = 0 
p_normal_ocupados = 0 

# Acumuladores
taquilla_VIP = 0
taquilla_normal = 0

"""
Programa principal
"""

# Ciclo de venta de entradas
while (p_normal_ocupados + p_VIP_ocupados < PUESTOS_VIP + PUESTOS_NORMAL):
    # Estado del cine
    print(" CINE DE SPRINGFIELD")
    print("- Puestos VIP disponibles: ", PUESTOS_VIP - p_VIP_ocupados)
    print("- Puestos normales disponibles: ", PUESTOS_NORMAL - p_normal_ocupados)

    # Solicitud del tipo de entrada
    tipo_puesto = int(input("\nIngrese el tipo de puesto (1: VIP, 2: Normal, 3: Salir): "))
    # Seleccion del tipo de puesto
    if (tipo_puesto == VIP):
        # Entrada VIP
        if (p_VIP_ocupados < PUESTOS_VIP):
            # Hay puesto VIP 
            p_VIP_ocupados = p_VIP_ocupados + 1
            taquilla_VIP = taquilla_VIP + VALOR_VIP          
        else:
            # No hay puesto VIP
            print("No hay puesto VIP\n")          
    elif (tipo_puesto == NORMAL):
        # Entrada Normal
        if (p_normal_ocupados < PUESTOS_NORMAL):
            # Hay puesto normal
            p_normal_ocupados = p_normal_ocupados + 1
            taquilla_normal = taquilla_normal + VALOR_NORMAL
        else:
            # No hay puesto normal
            print("No hay puesto normal\n")          
    elif (tipo_puesto == SALIR):
        # Ruptura del ciclo (El usuario selecciono salir)
        break  
    else: 
        # Opcion invalida
        print("ERROR: Opcion invalida.\n")


# Mensaje de salida del ciclo que indica el inicio de la funcion de cine
print("Empieza la funcion...")
  
# Calculo de estadisticas
porc_lleno_VIP = p_VIP_ocupados / PUESTOS_VIP * 100
porc_lleno_Normal = p_normal_ocupados / PUESTOS_NORMAL * 100
total_taquilla = taquilla_VIP + taquilla_normal

# Despliegue de la informacion de la funcion  
print("------------------------------------------------ Totales ------------------------------------------------")
print(f"- Porcentaje de puestos VIP ocupados ({p_VIP_ocupados}/{PUESTOS_VIP}): {porc_lleno_VIP:.2f}%")
print(f"- Puestos normales ocupados ({p_normal_ocupados}/{PUESTOS_NORMAL}): {porc_lleno_Normal:.2f}%")
print(f"- Total en taquilla VIP: {taquilla_VIP}")
print(f"- Total en taquilla Normal: {taquilla_normal}")
print(f"- Total en taquilla: {total_taquilla}")
print("---------------------------------------------------------------------------------------------------------")