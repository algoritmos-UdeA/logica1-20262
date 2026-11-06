# Punto 2: Ambulancias (Forma 1)

# Coordenada de la emergencia
x_emerg = float(input("Ingrese la coordenada x de la emergencia: "))
y_emerg = float(input("Ingrese la coordenada y de la emergencia: "))
# Numero de ambulancias
N = int(input("Ingrese el número de ambulancias N: "))
d_min = 999999999 # Distancia minima (inicialmente muy grande)
for i in range(N):
    # Entrada de las coordenadas de la i-esima ambulancia
    x_amb = float(input(f"Coordenada x de la ambulancia {i+1}: "))
    y_amb = float(input(f"Coordenada y de la ambulancia {i+1}: "))
    # Calculo de la distancia
    d = ((x_emerg - x_amb)**2 + (y_emerg - y_amb)**2)**0.5 
    # Actualizacion de la distancia minima
    if d < d_min:
        d_min = d
        x_min = x_amb
        y_min = y_amb
print(f"Ambulancia más cercana: ({x_min}, {y_min})")
print(f"Distancia: {d_min}")

      





