![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Conversión de temperatura en varios archivos

## Qué hace

> Un programa con menú convierte temperaturas de grados Celsius a Fahrenheit y a Kelvin. Las funciones de conversión van en un módulo propio, `conversiones.py`, y el programa principal lo importa.

Son los pasos de las diapositivas 47 a 54 de la [clase 10](../../../README.md): cómo se pasa de un programa en un archivo a uno en **varios archivos**, y dónde poner las pruebas para que no se ejecuten cada vez que alguien importa el módulo. Cada subcarpeta es un paso, y cada una funciona sola.

Para verlo explicado en clase, paso a paso: [sesión magistral 26](../../../sesion_magistral-26/README.md).

## Los archivos

```
📁 temperaturas_modulos/
   📁 0_name/ — qué es __name__
      📄 saludo.py
      📄 principal.py — importa saludo
   📁 1_sin_guarda/ — las pruebas al final del módulo, sin guarda
      📄 conversiones.py
      📄 main.py — importa conversiones
   📁 2_con_guarda/ — opción 1: las pruebas dentro de if __name__ == "__main__":
      📄 conversiones.py
      📄 main.py
   📁 3_archivo_pruebas/ — opción 2: las pruebas en su propio archivo
      📄 conversiones.py
      📄 test_conversiones.py
      📄 main.py
```

| Paso | Qué muestra |
|---|---|
| [0_name/](0_name/) | `__name__` vale `"__main__"` en el archivo que se ejecuta, y el nombre del módulo (`"saludo"`) cuando el archivo se importa |
| [1_sin_guarda/](1_sin_guarda/) | El problema: como `import` ejecuta todo el módulo, las pruebas de `conversiones.py` se ejecutan también al abrir el menú |
| [2_con_guarda/](2_con_guarda/) | **Opción 1:** las pruebas van dentro de la guarda `if __name__ == "__main__":`, y `main.py` agrupa el programa en `def main()` con su propia guarda |
| [3_archivo_pruebas/](3_archivo_pruebas/) | **Opción 2:** `conversiones.py` solo tiene funciones y las pruebas están en `test_conversiones.py`. Es la organización que se usa desde el [laboratorio 4](../../../../../laboratorios/4/README.md) |

## Cómo ejecutarlo

Cada paso se ejecuta **desde su propia carpeta**:

```
cd clases/10/teoria/codigo/temperaturas_modulos/0_name
python saludo.py
python principal.py

cd ../1_sin_guarda
python main.py

cd ../2_con_guarda
python conversiones.py
python main.py

cd ../3_archivo_pruebas
python test_conversiones.py
python main.py
```

## Salida esperada

**Paso 0.** El mismo `print` de `saludo.py` da dos resultados distintos:

```
> python saludo.py
En saludo.py, __name__ vale: __main__

> python principal.py
En saludo.py, __name__ vale: saludo
En principal.py, __name__ vale: __main__
```

**Paso 1.** Al abrir el menú aparece un mensaje que no debería estar: es de las pruebas de `conversiones.py`.

```
> python main.py
Pruebas de conversiones: todas pasaron
Programa de conversion de °C a °F y °K
--------------------------------
1. °C a °F
2. °C a °K
3. Salir

Elija una opcion: 1
Digite la temperatura en °C: 100
100.0°C = 212.00°F
...
Elija una opcion: 3
Gracias por usarnos
```

**Paso 2.** Las pruebas solo se ejecutan cuando se corre `conversiones.py`; el menú ya no las muestra.

```
> python conversiones.py
Pruebas de conversiones: todas pasaron

> python main.py
Programa de conversion de °C a °F y °K
--------------------------------
...
```

**Paso 3.** Las pruebas están en su propio archivo, y `conversiones.py` ya no imprime nada si se ejecuta solo. Una sesión con las dos conversiones y una opción inválida:

```
> python test_conversiones.py
Pruebas de conversiones: todas pasaron

> python main.py
Programa de conversion de °C a °F y °K
--------------------------------
1. °C a °F
2. °C a °K
3. Salir

Elija una opcion: 1
Digite la temperatura en °C: 100
100.0°C = 212.00°F
...
Elija una opcion: 2
Digite la temperatura en °C: -273.15
-273.15°C = 0.00°K
...
Elija una opcion: 5
ERROR: Opcion no valida
...
Elija una opcion: 3
Gracias por usarnos
```

## Si algo falla

| Lo que pasa | Por qué | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: No module named 'conversiones'` | Se ejecutó desde otra carpeta | Entrar a la carpeta del paso antes de ejecutar |
| Los cambios en `conversiones.py` no se notan | Se editó el `conversiones.py` de **otro** paso: cada carpeta tiene su propia copia | Editar el archivo de la carpeta desde la que se ejecuta |
| Aparece una carpeta `__pycache__/` | Python guarda ahí una versión compilada de los módulos importados | Es normal; se puede borrar y no se sube al repositorio |

> [!Important]
> Se usó IA generativa para redactar esta guía a partir del código de la clase. Las salidas son de ejecuciones reales. El docente revisa y valida la versión final.
