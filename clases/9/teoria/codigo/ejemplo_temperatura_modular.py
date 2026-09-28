def celsius_a_fahrenheit(c):
    f = (9 / 5) * c + 32
    return f


temp_c = float(input("Ingrese los °C: "))
temp_f = celsius_a_fahrenheit(temp_c)

print(f"{temp_c} °C = {temp_f} °F")

