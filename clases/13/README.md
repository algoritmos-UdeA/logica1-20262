![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 13 — Programación orientada a objetos (POO)

Continuación de la [clase 12](../12/README.md), que cerró con el programa de **administración de notas de un curso** resuelto con tres arreglos paralelos (`ids`, `nombres` y `notas`) parcialmente llenos. El programa funciona, pero deja varias incomodidades: un estudiante no existe como tal (son tres datos sueltos que comparten una posición), cada intercambio son tres, la variable `cantidad` tiene que viajar a todas partes, y si mañana se agrega el correo, cambian varias funciones. La **programación orientada a objetos** propone otra forma de pensar el problema: los datos y lo que se hace con ellos viven juntos, en un **objeto**. Una **clase** es el plano (qué datos tiene y qué sabe hacer) y cada objeto es una casa construida con ese plano, con sus propios valores.

La clase se divide en dos bloques. El **bloque 1** va del problema al lenguaje: qué es un objeto y qué es una clase, cómo se dibuja una clase en **UML** y cómo se pasa de UML a Python (`class`, `__init__`, `self`, atributos privados con `__`, *getters* y *setters*, `__str__`). Se trabaja con cinco ejemplos que crecen poco a poco: un rectángulo, un ventilador, un celular, una cuenta bancaria con su titular y un arreglo de cuentas, que termina convertido en la clase `Banco`. El **bloque 2** retoma el problema de la clase 12 con las clases `Estudiante` y `Curso` y el mismo menú; en las diapositivas solo aparece su diagrama UML. La herencia y el polimorfismo quedan fuera del alcance del curso.

## Teoría

- [`teoria/README.md`](teoria/README.md) — resumen del tema completo: paradigmas de programación, clase y objeto, estado, comportamiento e identidad, encapsulamiento, UML y su paso a Python, los ejemplos del bloque 1, las relaciones entre clases (asociación, composición y agregación), el diagrama del bloque 2 y los errores típicos, con la descripción de cada diagrama y de cada script.
- [`teoria/clase-13.pdf`](teoria/clase-13.pdf) / [`teoria/clase-13.pptx`](teoria/clase-13.pptx) — diapositivas completas (67 diapositivas).
- [`teoria/codigo/README.md`](teoria/codigo/README.md) — **índice del código**: el enunciado de cada ejemplo y los enlaces a los archivos que lo resuelven.
- [`teoria/codigo/`](teoria/codigo/) — los scripts de los ejemplos:
  - `ej1_rectangulo.py` y `ej1_rectangulo_privado.py`: el rectángulo con atributos públicos y luego privados.
  - `ej2_ventilador.py`: constantes de clase, valores por defecto y `__str__`.
  - `ej3_celular.py`: el ejercicio "Hágalo usted mismo".
  - `ej4_cuenta_titular.py`: dos clases relacionadas, `Titular` y `CuentaBancaria`.
  - `ej5_arreglo_cuentas.py`: un arreglo de cuentas.
  - `ej6_banco.py`: la clase `Banco`, que guarda el arreglo de cuentas.

## Aplicaciones completas: estructurada frente a POO

Dos programas completos, cada uno resuelto **dos veces**: con programación estructurada y con POO. Tienen el mismo comportamiento, la misma organización en archivos y una página que los compara paso a paso. Conviene estudiarlos después del bloque 1.

- [`teoria/app_curso/`](teoria/app_curso/README.md) — **la administración de notas de un curso**: el integrador de la clase 12 (arreglos paralelos) frente a las clases `Estudiante` y `Curso`. Es el **bloque 2 implementado**: lo que en las diapositivas solo aparece como diagrama UML, aquí está programado y probado. Muestra la **agregación**.
- [`teoria/app_piedra-papel-tijera/`](teoria/app_piedra-papel-tijera/README.md) — **el juego de piedra, papel o tijera** de la clase 10, convertido en una partida a 3 rondas: funciones y variables sueltas frente a las clases `Jugador`, `Ronda` y `Partida`. Muestra cómo crece un diseño y reúne las tres relaciones: **asociación, agregación y composición**.

En las dos, la versión POO termina con una sección sobre **cómo usa las clases el programa principal** (el "cliente"), con un adelanto del diagrama de secuencia.

Hay una tercera aplicación, resuelta solo con POO, para estudiar **cómo se diseña y se construye un programa con varias clases**:

- [`teoria/app_transporte/`](teoria/app_transporte/README.md) — **una plataforma de transporte** que le asigna a cada cliente el conductor disponible más cercano, con las clases `Punto`, `Cliente`, `Conductor`, `Viaje` y `Plataforma`. Su README es un **manual de usuario**: cómo ejecutarla, qué hace cada opción del menú y una sesión de ejemplo. El diseño se explica paso a paso en el notebook [De una clase a varias](sesion_magistral-32/notebooks/aplicacion_transporte.ipynb): del enunciado a las clases, cada clase probada antes de la siguiente, y la integración. Usa las listas con sus métodos (`append`).

## Sesiones magistrales

| Sesión | Fecha | Modalidad | Contenido cubierto | Detalle |
|---|---|---|---|---|
| 32 | Mar 10 nov (bloques 1 y 2, 14-18) | 🏫 Presencial | El bloque 1 completo: todo dato es un objeto, paradigmas, clase y objeto, UML y su paso a Python, y cinco ejemplos que crecen (rectángulo, ventilador, celular, cuenta bancaria con su titular y un arreglo de cuentas) hasta la clase `Banco`; composición y agregación, el UML del bloque 2 y errores típicos. Con un notebook complementario a las diapositivas. Ocupa los dos bloques del día | [sesion_magistral-32](sesion_magistral-32/README.md) |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir del material de la clase. El docente revisó y validó la versión final.
