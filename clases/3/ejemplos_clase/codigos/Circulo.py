#Definir variables
PI=3.14
radio=float
perimetro=float
area=float

#Pedir dato
radio=float(input("Ingrese el radio del círculo (en cm): "))
	
#Calcular área y perímetro
area=PI*radio**2
perimetro=2*PI*radio
	
print(f"El área del círculo es {area} y su perimetro es {perimetro}")