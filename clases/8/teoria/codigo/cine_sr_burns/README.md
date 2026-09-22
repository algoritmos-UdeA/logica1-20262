# Ejemplo 

El siguiente ejemplo permite repasar algunos de los conceptos vistos previamente.

## Cine del Sr. Burns

### Enunciado

El señor Burns, como buen capitalista que es, decidió construir un cine en Springfield. El cine es pequeño: tiene capacidad para 8 puestos VIP (a $7000 cada uno) y 40 puestos normales (a $5000 cada uno).

Para cada función, el señor Burns no sabe de antemano cuántos clientes van a asistir — puede que se llenen todos los puestos, o que la venta se cierre antes con puestos disponibles. Desarrolle una aplicación que:
* Registre la venta de una boleta solicitando al cajero el tipo de puesto (VIP o normal), y repita este registro hasta que ocurra una de estas dos condiciones: se agoten los 48 puestos, o el cajero ingrese -1 como tipo de puesto para indicar que no hay más clientes y cerrar la venta.
* Si el tipo de puesto solicitado ya alcanzó su capacidad máxima, no contabilizar esa venta, informarlo al cajero, y volver a solicitar el tipo de puesto (sin que esto se interprete como el cierre de la venta)
* Obtener, para cada tipo de puesto, el total de asistentes y la ganancia obtenida.
* Cuando se cierre la venta de boletas para la función (por cualquiera de las dos condiciones anteriores), imprimir el total de asistentes y las siguientes estadísticas:
  * El porcentaje de ocupación de cada zona (qué porcentaje de la capacidad VIP y de la capacidad Normal se logró vender).
  * El dinero total recaudado por las entradas VIP, por las entradas Normales y la taquilla total del cine.

## Solición:

### Entradas

Se tiene que solicitar *por cada cliente* el tipo de boleta (VIP o Normal) para ir al cine. En nuestro caso se va a emplear el 1 para la boleta en la zona VIP, el 2 para la boleta en la zona normal y el 3 para salir del menu (ciclo) por que va a empezar la pelicula y ya no se venderan mas entradas.

### Salidas

Estadisticas asociadas a la taquilla (Sillas ocupadas de cada tipo con su porcentaje asociado y total de ventas (VIP, Normal, ambos)).

### Definición de variables

* VALOR_VIP = 7000
* VALOR_NORMAL = 5000
* PUESTOS_VIP = 8
* PUESTOS_NORMAL = 40
* tipo_puesto: Tipo de puesto (1: VIP; 2: Normal; 3: Salir)
* p_VIP_ocupados: Puestos VIP ocupados
* p_normal_ocupados: Puestos Normales ocupados
* taquilla_VIP: Total recaudado en los puestos VIP
* taquilla_normal: Total recaudado por los puestos normales
* total_taquilla: Taquilla normal
* p_asistentes: Porcentaje de asistentes

## Implementación

### Pseudocodigo

```
Inicio
  # Opciones
  VIP = 1
  NORMAL = 2
  SALIR = 3
  
  # Precios
  VALOR_VIP = 7000
  VALOR_NORMAL = 5000
  
  # Capacidad cine
  PUESTOS_VIP = 8
  PUESTOS_NORMAL = 40
  
  # Variables
  p_VIP_ocupados = 0 
  p_normal_ocupados = 0 
  taquilla_VIP = 0
  taquilla_normal = 0

  # Ciclo principal
  Mientras (p_normal_ocupados + p_VIP_ocupados < PUESTOS_VIP + PUESTOS_NORMAL) Haga:
    # Estado del cine
    Escribir(PUESTOS_NORMAL - p_normal_ocupados, PUESTOS_VIP - p_VIP_ocupados)
    # Solicitud del tipo de entrada
    Leer(tipo_puesto)
    
    Si (tipo_puesto == VIP) Entonces
      # Opcion 1: Entrada VIP
      Si (p_VIP_ocupados < PUESTOS_VIP)
          # Hay puesto VIP 
          p_VIP_ocupados = p_VIP_ocupados + 1
          taquilla_VIP = taquilla_VIP + VALOR_VIP          
        SiNo
          # No hay puesto VIP
          Escribir("No hay puesto VIP")          
        Fin_Si
    SiNo
      Si (tipo_puesto == NORMAL) Entonces        
        # Opcion 2: Entrada Normal
        Si (p_normal_ocupados < PUESTOS_NORMAL)
          # Hay puesto normal
          p_normal_ocupados = p_normal_ocupados + 1
          taquilla_normal = taquilla_normal + VALOR_NORMAL
        SiNo
          # No hay puesto normal
          Escribir("No hay puesto normal")          
        Fin_Si
      SiNo
        Si (tipo_puesto == SALIR) Entonces
          # Opcion -1: Salir          
          Romper # Ruptura del ciclo (El usuario selecciono salir)
        SiNo
          # Otro numero: Opcion invalida
          Escriba("ERROR: Opcion invalida")
        Fin_Si
      Fin_Si
    Fin_Si
  Fin_Mientras
  
  Escribir("Empieza la funcion...")
  
  # Estadisticas exigidas  
  porc_lleno_VIP = p_VIP_ocupados / PUESTOS_VIP * 100
  porc_lleno_Normal = p_normal_ocupados / PUESTOS_NORMAL * 100
  total_taquilla = taquilla_VIP + taquilla_normal
  
  Escribir("---- Totales ----")
  Escribir(porc_lleno_VIP, porc_lleno_Normal, taquilla_VIP, taquilla_normal, total_taquilla)
  Escribir("-----------------")
Fin
```

### Python

La solución en python se encuentra en [ejemplo_cine.py](ejemplo_cine.py) cuyo codigo se muestra a continuación:

```python
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
```

## Verificación

Como casos de prueba se emplean los siguientes casos de test cambiando las constantes asociadas a las dimensiones del cine por valore mas pequeños para realizar las pruebas (`PUESTOS_VIP = 2` y `PUESTOS_NORMAL = 4`).

|Caso|tipo_puesto|Caso|
|1|1,2,1,2,2,2|Cine lleno|
|2|1,1,3|VIP lleno, Normal vacio|
|3|2,2,2,4,2,3|Normal lleno, VIP vacio, error en el menu de entrada (x1)|
|4|-2,1,2,2,2,3|Normal al 75%, VIP al 50% , error en el menu de entrada (x1)|
|5|4,5,3|Error en el menu de entrada (x2), cine vacio|

A continuación se muestra la salida para el caso de test 4:

```
 CINE DE SPRINGFIELD
- Puestos VIP disponibles:  2
- Puestos normales disponibles:  4

Ingrese el tipo de puesto (1: VIP, 2: Normal, 3: Salir): -2
ERROR: Opcion invalida.

 CINE DE SPRINGFIELD
- Puestos VIP disponibles:  2
- Puestos normales disponibles:  4

Ingrese el tipo de puesto (1: VIP, 2: Normal, 3: Salir): 1
 CINE DE SPRINGFIELD
- Puestos VIP disponibles:  1
- Puestos normales disponibles:  4

Ingrese el tipo de puesto (1: VIP, 2: Normal, 3: Salir): 2
 CINE DE SPRINGFIELD
- Puestos VIP disponibles:  1
- Puestos normales disponibles:  3

Ingrese el tipo de puesto (1: VIP, 2: Normal, 3: Salir): 2
 CINE DE SPRINGFIELD
- Puestos VIP disponibles:  1
- Puestos normales disponibles:  2

Ingrese el tipo de puesto (1: VIP, 2: Normal, 3: Salir): 2
 CINE DE SPRINGFIELD
- Puestos VIP disponibles:  1
- Puestos normales disponibles:  1

Ingrese el tipo de puesto (1: VIP, 2: Normal, 3: Salir): 3
Empieza la funcion...
------------------------------------------------ Totales ------------------------------------------------
- Porcentaje de puestos VIP ocupados (1/2): 50.00%
- Puestos normales ocupados (3/4): 75.00%
- Total en taquilla VIP: 7000
- Total en taquilla Normal: 15000
- Total en taquilla: 22000
---------------------------------------------------------------------------------------------------------
```

