![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Idea de laboratorio: reservas de un vuelo

Problema integrador de arreglos (clases 11 y 12) que se preparó para el [Taller 4 — Arreglos](../talleres/arreglos/README.md) y se retiró de allí el 11/11/2026 para usarlo más adelante como laboratorio. Está adaptado del ejercicio del vuelo Madrid – Caracas de Joyanes (las plazas de fumadores y no fumadores se cambiaron por clase ejecutiva y económica). Usa un arreglo de valores lógicos de tamaño fijo, búsqueda lineal y funciones del caso 3 que además retornan un valor, sin métodos de listas.

Los casos de prueba de la tabla se verificaron con una solución de referencia (no incluida) para un avión de 6 asientos.

## Enunciado

Se desea elaborar un programa que permita controlar las reservas de asientos de un vuelo Medellín – Madrid, de acuerdo con las siguientes normas de la aerolínea:

* Número de asientos del avión: 300.
* Asientos numerados de 1 a 100: clase ejecutiva.
* Asientos numerados de 101 a 300: clase económica.

El programa muestra un menú que se repite hasta que se cierran las reservas:

```text
1. Reservar un asiento
2. Anular una reserva
3. Mostrar asientos libres
0. Cerrar las reservas (el avión va a despegar)
```

* **Reservar:** se pregunta la clase (1: ejecutiva, 2: económica) y se le asigna al pasajero el asiento libre **de menor número** de esa clase. Si la clase está llena, se informa.
* **Anular:** se pide el número del asiento. Si estaba reservado, queda libre; si no estaba reservado o el número no existe, se informa.
* **Mostrar asientos libres:** muestra cuántos asientos libres hay en cada clase.
* Las reservas se cierran cuando el usuario elige la opción 0 **o** cuando el avión queda lleno.

Diseñe el programa con funciones. Una posible división es:

| Función | Qué hace | Caso |
|---|---|---|
| `buscar_libre(ocupado, primero, ultimo)` | Retorna el número del primer asiento libre entre `primero` y `ultimo`, o `-1` si no hay | 1 |
| `reservar(ocupado, primero, ultimo)` | Marca como ocupado el primer asiento libre de ese rango y retorna su número, o `-1` | 3 (y retorna un valor) |
| `anular(ocupado, asiento)` | Libera el asiento y retorna `True`; si no se puede, retorna `False` sin cambiar nada | 3 (y retorna un valor) |
| `contar_libres(ocupado, primero, ultimo)` | Retorna cuántos asientos libres hay en ese rango | 1 |

El arreglo `ocupado` tiene un valor lógico por asiento: `ocupado = [False] * ASIENTOS`.

> [!Tip]
> **Pista:** el asiento número 1 está en la posición 0, así que el asiento `a` está en `ocupado[a - 1]`. Para probar, use constantes y cámbielas por un avión pequeño: `ASIENTOS = 6`, ejecutiva de 1 a 2 y económica de 3 a 6.

Casos de prueba con el avión pequeño, en este orden:

| Paso | Acción | Resultado esperado |
|---|---|---|
| 1 | Reservar en ejecutiva | Asiento 1 |
| 2 | Reservar en ejecutiva | Asiento 2 |
| 3 | Reservar en ejecutiva | No hay asientos libres en ejecutiva |
| 4 | Reservar en económica | Asiento 3 |
| 5 | Anular el asiento 1 | Reserva anulada |
| 6 | Reservar en ejecutiva | Asiento 1 (otra vez) |
| 7 | Anular el asiento 5 | El asiento 5 no está reservado |
| 8 | Anular el asiento 9 | El asiento 9 no existe |
| 9 | Mostrar asientos libres | Ejecutiva: 0, económica: 3 |
| 10 | Reservar en económica tres veces | Asientos 4, 5 y 6; el avión queda lleno y se cierran las reservas |

> **Pregunta para pensar:** ¿es `ocupado` un arreglo parcialmente lleno, como los de la [sección 3 del Taller 4](../talleres/arreglos/README.md#3-arreglos-parcialmente-llenos)? ¿Por qué aquí no se necesita una variable `cantidad`?

---

> [!Important]
> Se usó IA generativa para adaptar y organizar este enunciado a partir de un taller de repaso anterior y de las indicaciones del docente. Los casos de prueba se verificaron ejecutando el código. El docente revisó y validó la versión final.
