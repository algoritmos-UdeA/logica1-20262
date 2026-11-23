![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Repaso: un programa en tres archivos

## Qué hace

> Convertir una temperatura de grados Celsius a grados Fahrenheit.

Es el repaso con el que empieza la [clase 11](../../../README.md) (diapositivas 5 a 7): la organización en tres archivos de la clase 10, con una sola función. Sirve como plantilla mínima de esa organización.

## Los archivos

```
📁 repaso_funciones/
   📄 conversiones.py — la función, con su especificación (Supone / Garantiza)
   📄 test_conversiones.py — las pruebas con assert
   📄 main.py — el programa principal: def main() y la guarda
```

| Archivo | Contenido |
|---|---|
| [conversiones.py](conversiones.py) | Solo la función `celsius_a_fahrenheit(temp_c)` |
| [test_conversiones.py](test_conversiones.py) | Importa el módulo, prueba la función con `assert` y termina con un mensaje |
| [main.py](main.py) | Pide una temperatura en °C y muestra su equivalente en °F |

## Cómo ejecutarlo

```
cd clases/11/teoria/codigo/repaso_funciones
python test_conversiones.py
python main.py
```

## Salida esperada

```
> python test_conversiones.py
Pruebas de conversiones: todas pasaron

> python main.py
Ingrese los °C: 100
100.0 °C = 212.00 °F
```

## Si algo falla

| Lo que pasa | Por qué | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: No module named 'conversiones'` | Se ejecutó desde otra carpeta | Entrar a la carpeta `repaso_funciones` antes de ejecutar |
| `ValueError: could not convert string to float` | Se escribió la temperatura con coma (`36,5`) | Escribirla con punto: `36.5` |

> [!Important]
> Se usó IA generativa para redactar esta guía a partir del código de la clase. Las salidas son de ejecuciones reales. El docente revisa y valida la versión final.
