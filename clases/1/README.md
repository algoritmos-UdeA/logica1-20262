![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 1 - Conociendo las Herramientas de Trabajo

Sección de recursos para comenzar a programar: herramientas requeridas, entornos de práctica en línea y actividades de calentamiento para desarrollar una noción intuitiva de la codificación antes de entrar de lleno al curso.

---

## Teoría

- [`teoria/README.md`](teoria/README.md) — resumen del tema: computador, hardware/software, algoritmos y lenguajes de programación.
- [`teoria/clase-01.pdf`](teoria/clase-01.pdf) / [`teoria/clase-01.pptx`](teoria/clase-01.pptx) — diapositivas completas.

## Sesiones magistrales

| Sesión | Fecha | Modalidad | Contenido cubierto | Detalle |
|---|---|---|---|---|
| 2 | Mar 4 ago (bloque 1, 14-16) | 🏫 Presencial | Teoría del tema completa | [sesion_magistral-2](sesion_magistral-2/README.md) |

---

## Objetivos

- Instalar y configurar las herramientas necesarias para el desarrollo del curso.
- Reconocer los entornos y plataformas que se utilizarán para practicar y visualizar la ejecución de programas.
- Desarrollar una noción intuitiva de qué significa programar, a través de actividades gamificadas, antes de escribir código en Python.
- Relacionar, de forma preliminar, los conceptos de secuencia, condicionales y ciclos con su representación en un entorno de programación real.

---

## 1. Herramientas necesarias

Para el desarrollo del curso se requiere instalar un conjunto mínimo de herramientas en el computador. A continuación se explica para qué sirve cada una y dónde descargarla.

| Herramienta | ¿Para qué sirve? | Instalación |
|---|---|---|
| **Anaconda** | Distribución de Python que incluye el intérprete, el gestor de paquetes `conda` y Jupyter Notebook. Es la forma más sencilla de tener Python funcionando en el computador sin configuraciones adicionales. | Obligatoria |
| **Visual Studio Code (VS Code)** | Editor de código liviano donde se escribirán y ejecutarán los programas en Python durante todo el curso. Se usará la extensión oficial de Python para tener autocompletado, depuración y ejecución de scripts. | Obligatoria |
| **draw.io (diagrams.net)** | Herramienta para construir diagramas de flujo y esquemas que apoyan el diseño de un algoritmo antes de escribir el código. | Obligatoria |
| **PyCharm** | Entorno de desarrollo (IDE) especializado en Python, con herramientas más avanzadas de depuración y gestión de proyectos. Es una alternativa a VS Code para quien prefiera un entorno más completo. | Opcional |

> **Nota:** Anaconda, VS Code y draw.io son de instalación obligatoria antes de la primera clase de laboratorio. PyCharm es opcional y solo se recomienda si ya tiene experiencia previa con IDEs o desea explorar otro entorno de trabajo.

### 1.1 Instalar Anaconda

Se debe instalar **Anaconda**, ya que es la distribución de Python que se utilizará como base durante todo el curso.

- Página de descarga: **https://www.anaconda.com/download**

Seleccione el instalador correspondiente a su sistema operativo (Windows, macOS o Linux) y siga el asistente de instalación con las opciones predeterminadas.

### 1.2 Instalar draw.io

Se debe instalar **draw.io Desktop**, la herramienta que se utilizará para construir diagramas de flujo y esquemas de apoyo al diseño de algoritmos.

- Página de descarga: **https://get.diagrams.net**

También está disponible una versión en línea, sin necesidad de instalación, en **https://app.diagrams.net**.

### 1.3 Instalar Visual Studio Code

Se debe instalar **Visual Studio Code**, el editor que se usará para escribir y ejecutar el código Python del curso.

- Página de descarga: **https://code.visualstudio.com/download**

Una vez instalado, se recomienda agregar la extensión oficial **Python** (de Microsoft) desde el panel de extensiones.

### 1.4 Instalar PyCharm (opcional)

Como alternativa a VS Code, puede instalar **PyCharm**, un IDE especializado en Python desarrollado por JetBrains.

- Página de descarga: **https://www.jetbrains.com/pycharm/download**

---

## 2. Herramientas en línea (sin instalación)

Estas herramientas funcionan directamente en el navegador y son útiles para reforzar la comprensión de cómo se ejecuta un programa, sin necesidad de instalar nada.

| Herramienta | ¿Para qué sirve? | Enlace |
|---|---|---|
| **Python Tutor** | Visualiza paso a paso la ejecución de un programa: cómo cambian las variables, cómo se recorren los ciclos y cómo se llaman las funciones. Muy útil para entender el flujo de un algoritmo. | https://pythontutor.com |
| **CodeSkulptor** | Entorno interactivo de Python en el navegador, pensado para principiantes; permite escribir y ejecutar código sin configurar nada localmente. | https://py3.codeskulptor.org |

---

## 3. Links de utilidad para practicar

Estas plataformas se usarán a lo largo del curso para reforzar, mediante retos y gamificación, los conceptos vistos en clase. La columna de conceptos indica en qué momento del curso resulta más pertinente retomar cada plataforma.

| Plataforma | Enlace | Conceptos del curso que puede abordar |
|---|---|---|
| Code.org | https://code.org | Secuencias, condicionales simples y dobles, ciclos (`while`, `for`) |
| CodeCombat | https://codecombat.com | Algoritmos secuenciales, condicionales, ciclos y ciclos anidados |
| Codewars | https://www.codewars.com | Condicionales, ciclos, arreglos unidimensionales y bidimensionales |
| Exercism | https://exercism.org | Programación orientada a objetos, arreglos y buenas prácticas de código |
| CodinGame | https://www.codingame.com | Ciclos anidados, arreglos, búsqueda y ordenamiento |

---

## 4. Actividades — Desarrollo de la noción intuitiva de codificación

Antes de escribir la primera línea de código en Python, es importante desarrollar una intuición sobre qué significa "programar": dar instrucciones precisas y ordenadas para que un sistema resuelva un problema. Para ello, se solicita realizar las siguientes actividades de Code.org, diseñadas para introducir estos conceptos de forma visual y gamificada, sin requisitos previos de programación.

1. **Classic Maze** — introducción a la secuencia de instrucciones y a los ciclos básicos.
   Enlace: https://studio.code.org/hoc/1

2. **Flappy Code** — construcción de un pequeño videojuego aplicando eventos y condicionales.
   Enlace: https://studio.code.org/s/flappy

3. **Minecraft: Hero's Journey** — resolución de retos progresivos que combinan secuencias, ciclos y condicionales en un entorno familiar para los estudiantes.
   Enlace: https://studio.code.org/courses/hero/units/1

> Estas actividades no requieren instalación ni cuenta obligatoria y toman aproximadamente entre 10 y 45 minutos cada una. Se recomienda completarlas antes de la primera sesión de laboratorio del curso.

---

## 5. Checklist de verificación

Utilice esta lista para llevar el control de las herramientas instaladas y las actividades completadas antes de la primera sesión de laboratorio.

**Instalación de herramientas**

- [ ] Anaconda instalado y verificado
- [ ] Visual Studio Code instalado, con la extensión de Python
- [ ] draw.io instalado (o accesible en línea)
- [ ] PyCharm instalado (opcional)

**Reconocimiento de herramientas en línea**

- [ ] Python Tutor: probado con un ejemplo sencillo
- [ ] CodeSkulptor: probado con un ejemplo sencillo

**Actividades de Code.org**

- [ ] Classic Maze completada
- [ ] Flappy Code completada
- [ ] Minecraft: Hero's Journey completada

---

## Resultados de aprendizaje

Al completar esta clase, el estudiante estará en capacidad de:

- Contar con un entorno de trabajo local (Anaconda, VS Code y draw.io) listo para el desarrollo de algoritmos y programas en Python.
- Identificar y diferenciar las plataformas de práctica que apoyarán su proceso de aprendizaje a lo largo del curso, y con qué conceptos se relaciona cada una.
- Explicar, con sus propias palabras y a partir de las actividades gamificadas realizadas, qué es una secuencia de instrucciones y cómo se relaciona con la idea de un algoritmo.
- Reconocer, de forma intuitiva, patrones de decisión (condicionales) y repetición (ciclos) en un entorno de programación visual, como base para su formalización posterior en Python.

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de indicaciones del docente. El docente revisó y validó la versión final.
