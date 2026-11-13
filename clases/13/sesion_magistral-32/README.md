![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Sesion magistral 32

* **Tipo**: Presencial
* **Fecha**: 10/11/2026
* **Parte**: Primer y segundo bloque de clase (14-18)

## Resumen

Esta sesión cubre el bloque 1 de la [clase 13](../README.md), **programación orientada a objetos (POO)**. Parte del problema que dejó la clase 12: la administración de notas de un curso resuelta con arreglos paralelos funciona, pero un estudiante no existe como tal, cada intercambio son tres y la variable `cantidad` va a todas partes. La POO propone que los datos y lo que se hace con ellos vivan juntos, en un objeto.

| Parte | Tema |
|---|---|
| 0 | Repaso: los arreglos paralelos y el tablero de incomodidades |
| 1-3 | Todo dato es un objeto; paradigmas de programación; clase y objeto (estado, comportamiento e identidad) |
| 4 | Abstracción y encapsulamiento, UML y el paso de UML a Python |
| 5 | Ejemplo 1: `Rectangulo`, con atributos públicos y después privados, *getters* y *setters* que validan |
| 6 | Ejemplo 2: `Ventilador`, con constantes de clase, valores por defecto y `__str__` |
| 7 | Ejemplo 3: `Celular`, para hacerlo uno mismo |
| 8 | Ejemplo 4: `Titular` y `CuentaBancaria`, dos clases relacionadas (asociación) |
| 9 | Ejemplo 5: un arreglo de cuentas |
| 10 | Ejemplo 6: la clase `Banco`, que guarda el arreglo de cuentas (composición) |
| 11 | ¿Por qué POO?: el tablero con el banco, el diagrama UML del bloque 2 (`Estudiante` y `Curso`), y composición frente a agregación |
| 12 | Errores típicos |

## Notebook

[`notebooks/programacion_orientada_objetos.ipynb`](notebooks/programacion_orientada_objetos.ipynb) acompaña las diapositivas: reúne el código de la clase y la teoría más importante, para que el tema se pueda estudiar completo sin ellas. Se puede abrir en Google Colab con el botón **Open in Colab** que tiene al comienzo, o en Jupyter (las instrucciones para abrir un notebook están en la [sesión 19](../../8/sesion_magistral-19/README.md)).

Cada ejemplo sigue el mismo camino que en las diapositivas:

1. **el enunciado**, que dice qué datos tiene la clase y qué sabe hacer;
2. **el diagrama UML**, que la dibuja antes de escribirla;
3. **la clase en Python**, en su propia celda;
4. **el uso**: crear objetos y pedirles cosas;
5. **las pruebas** con `assert`, en una celda aparte, con su tabla de casos típicos, límite y especiales.

Además:

* **Errores frecuentes** que fallan a propósito: cambiar un atributo público sin control, intentar cambiar un atributo privado desde afuera, olvidar `self`, comparar objetos con `==` y escribir dos constructores.
* **Hágalo usted mismo**: la clase `Celular` se completa a partir de su diagrama UML, con las pruebas ya escritas. Esas dos celdas no tienen salida guardada, y la solución está oculta.
* **Para practicar**: cinco ejercicios con la solución oculta.
* Un enlace a **Python Tutor** debajo de cada celda de código, donde cada objeto se ve como una caja y cada variable como una flecha hacia su objeto.

El código de la clase, en archivos, está en [`teoria/codigo/`](../teoria/codigo/), con su índice en [`teoria/codigo/README.md`](../teoria/codigo/README.md).

## Notebook de la aplicación de transporte

En la sesión también se escribió, en vivo, un segundo notebook: la clase `Rectangulo` con atributos públicos y después privados, y el comienzo de una **aplicación de transporte** con las clases `Punto` y `Cliente`.

| Notebook | Qué es |
|---|---|
| [`notebooks/notebook_sin_editar/nov_10.ipynb`](notebooks/notebook_sin_editar/nov_10.ipynb) | El original de clase, tal como quedó |
| [`notebooks/aplicacion_transporte.ipynb`](notebooks/aplicacion_transporte.ipynb) | La versión ampliada, **De una clase a varias: una aplicación de transporte**, para estudiar sin haber asistido |

La versión ampliada se concentra en lo que más cuesta cuando el problema crece: **cómo se relacionan varias clases y cómo se juntan en un programa**.

| Parte | Tema |
|---|---|
| 0 | Repaso: una clase sola (`Rectangulo`) |
| 1 | La lista es un objeto: la clase `list` en UML, sus métodos (`append`, `pop`, `remove`, `sort`…) y la diferencia con la lista usada como arreglo |
| 2 | El problema: el enunciado y un caso calculado a mano |
| 3 | El diseño: de los sustantivos y los verbos del enunciado a las clases, sus métodos y sus relaciones, con el diagrama UML completo |
| 4-8 | La construcción, una clase a la vez y cada una con sus pruebas: `Punto`, `Cliente`, `Conductor`, `Viaje` y `Plataforma` |
| 9 | La integración: el programa principal, y una petición seguida de punta a punta por las cinco clases |
| 10 | Errores típicos al relacionar clases |
| 11 | Para practicar: cuatro ejercicios con la solución oculta y un reto |
| 12 | Referencias |

En cada relación se responden las mismas tres preguntas: **¿quién conoce a quién?, ¿quién crea el objeto?, ¿quién le pide qué a quién?**

La misma aplicación, separada en archivos y con un menú, está en [`teoria/app_transporte/`](../teoria/app_transporte/README.md), que incluye un manual de usuario.

> [!Important]
> Se usó IA generativa para preparar este contenido a partir de las diapositivas y el código de la clase. El docente revisó y validó la versión final.
