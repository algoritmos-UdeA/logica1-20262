"""
Programa principal (versiones 2 y 3).
"""
import conversiones


def main():
    print("Programa de conversion de °C a °F y °K")
    while True:
        print("--------------------------------")
        print("1. °C a °F")
        print("2. °C a °K")
        print("3. Salir")
        opcion = int(input("\nElija una opcion: "))
        if opcion == 1:
            temp_c = float(input("Digite la temperatura en °C: "))
            temp_f = conversiones.celsius_a_fahrenheit(temp_c)
            print(f"{temp_c}°C = {temp_f:.2f}°F\n")
        elif opcion == 2:
            temp_c = float(input("Digite la temperatura en °C: "))
            temp_k = conversiones.celsius_a_kelvin(temp_c)
            print(f"{temp_c}°C = {temp_k:.2f}°K\n")
        elif opcion == 3:
            print("Gracias por usarnos\n")
            break
        else:
            print("ERROR: Opcion no valida\n")


if __name__ == "__main__":
    main()
