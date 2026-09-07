![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 12

* **Tipo**: Presencial
* **Fecha**: 01/09/2026*
* **Parte**: Segundo bloque de clase (16-18)*

\* Fecha y bloque inferidos de las marcas de tiempo en los scripts de la sesión y de la numeración continua tras la sesión 11 (misma fecha, primer bloque) — pendiente de confirmar.

Primera sesión práctica del tema de ciclos [(teoría)](../teoria/): se introduce la estructura `while` en vivo con un ejemplo mínimo para observar cómo se comporta la variable de control, y luego se resuelve el problema de imprimir los números pares hasta `N` de dos formas equivalentes.

## Ejemplo 1 — `hola_ciclos`

Un primer contacto con el ciclo `while`, sin ningún problema de por medio: solo contar cuántas veces se repite el cuerpo e imprimir el valor final de la variable de control al salir.

**Código**: [hola_ciclos.py](hola_ciclos.py)

```py
N = 10
i = 0
while i<= N:      
    i = i + 1
    print("Hola")
print("Valor de i al salir:", i)
```

> **Para reflexionar:** aunque `N = 10`, `"Hola"` se imprime 11 veces y `i` termina en 11, no en 10. Como la actualización (`i = i + 1`) ocurre *antes* del `print`, la condición `i <= N` se evalúa todavía con `i = 10` (verdadera), así que el cuerpo se ejecuta una vez más de lo que parece a primera vista. Es el mismo tipo de error de conteo ("off-by-one") que se puede cometer al no fijarse en el orden exacto de las instrucciones dentro del cuerpo del ciclo.

## Ejemplo 2 — Serie de números pares hasta N

Dos formas de imprimir los números pares entre 0 y `N`, ambas partiendo de un contador (`num`) inicializado en 0.

### Forma 1 — filtrando con módulo

Se avanza de 1 en 1 y se filtra con el operador módulo (`%`) cuáles valores son pares.

**Código**: [serie_pares1.py](serie_pares1.py)

```py
N = int(input("Digite el numero: "))
num = 0
i = 0
while num <= N:
    if num%2 == 0:
        print(num)
    num += 1
```

### Forma 2 — avanzando de 2 en 2

Como se parte de `num = 0` (par), avanzar directamente de 2 en 2 genera solo números pares, sin necesidad de la condición con módulo.

**Código**: [serie_pares2.py](serie_pares2.py)

```py
N = int(input("Digite el numero: "))
num = 0
i = 0
while num <= N:
    print(num)
    num += 2
```

*Nota: ambos scripts dejan declarada una variable auxiliar `i` (junto con líneas comentadas que la incrementaban e imprimían) que ya no se usa en la versión final — un rastro de una versión anterior del ejemplo, útil para notar que Forma 2 llega al mismo resultado que Forma 1 con menos trabajo por iteración, al eliminar la comparación `num%2 == 0` a cambio de partir de un valor inicial par.*

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
