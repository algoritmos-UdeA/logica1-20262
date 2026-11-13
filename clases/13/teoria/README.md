![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Clase 13 — Programación orientada a objetos (Teoría)

Diapositivas base del tema 13, que continúa la [clase 12](../../12/teoria/README.md). Empiezan con un repaso del programa de administración de notas de un curso, resuelto con arreglos paralelos, y de las incomodidades que dejó. Luego presentan la programación orientada a objetos como otra forma de pensar el problema: qué es una clase y qué es un objeto, cómo se dibuja una clase en UML y cómo se pasa de UML a Python. Cinco ejemplos llevan del rectángulo más simple a un banco que guarda un arreglo de cuentas, y con él se comprueba cuáles incomodidades resolvieron los objetos. El cierre presenta el diagrama UML del bloque 2 (`Estudiante` y `Curso`), la diferencia entre composición y agregación, y los errores típicos. 67 diapositivas.

## Contenido cubierto

- **Apertura y repaso** (diapositivas 1-10): método de Polya, entrada → proceso → salida, y el programa integrador de la clase 12:
  - un curso de máximo `N = 10` estudiantes, con su Id (texto), su nombre y su nota, guardados en tres vectores paralelos (`ids`, `nombres` y `notas`) y una variable `cantidad`. El menú de siete opciones (agregar, eliminar, actualizar nota, buscar, listar, ordenar por nota y ordenar por nombre) está en [`clases/12/teoria/codigo/curso/`](../../12/teoria/codigo/curso/);
  - para ordenar, cada intercambio tiene que mover al estudiante completo: `intercambiar` se llama tres veces, una por vector. Si se olvida uno, los datos quedan mezclados y Python no avisa;
  - **el tablero de incomodidades**: un estudiante no existe como tal, cada intercambio son tres, `cantidad` va a todas partes, hay una función de ordenar por cada criterio, y agregar el correo cambiaría varias funciones. CS50x llega al mismo punto con una agenda guardada en dos arreglos paralelos (semana 3, *structs*);
  - **plan de la clase**: bloque 1, del problema al lenguaje; bloque 2, el curso con objetos.
- **Las ideas** (diapositivas 11-18):
  - **En Python, todo dato es un objeto**: una lista, un texto y un número tienen métodos propios, que se usan con la forma `objeto.metodo()` (`notas.append(4.0)`, `nombre.upper()`), y `type()` muestra de qué clase es cada uno. Lo nuevo es crear clases propias.
  - **Paradigmas de programación**: estructurada, funcional, orientada a objetos y reactiva, con lenguajes de ejemplo y una analogía (atender un restaurante: una receta, estaciones, roles o pedidos). En la programación estructurada los datos viajan de función en función como parámetros; en la POO viajan juntos con sus métodos, dentro del objeto. El mismo promedio de notas se calcula en los dos paradigmas y da 3.375.
  - **¿Cómo se guardan juntos datos de distinto tipo?**: un arreglo identifica cada dato por su posición y es de un solo tipo; un registro (`struct` en C) los identifica por su nombre; una clase, además, tiene métodos. Python admite listas con tipos mezclados, pero en el curso las listas se usan como arreglos.
  - **Clase y objeto**: la clase es el plano de una casa y cada objeto (o **instancia**) es una casa construida con ese plano, con sus propios valores. Todo objeto tiene **estado** (los valores de sus datos), **comportamiento** (lo que sabe hacer) e **identidad** (es uno solo, aunque tenga los mismos datos que otro: dos casas idénticas siguen siendo dos casas). Lo mismo se aplica a los estudiantes `lisa` y `bart`.
- **De la idea a UML y a Python** (diapositivas 19-25):
  - **Las cuatro propiedades de la POO**: abstracción, encapsulamiento, herencia y polimorfismo. En el curso solo se ven las dos primeras.
  - **Encapsulamiento**: los datos del objeto son privados y sus métodos son públicos; el código de afuera no toca los datos, le pide a un método lo que necesita (`get_nota()`, `set_nota()`).
  - **¿Por qué UML?**: la "guerra de los métodos" de 1989-1994, la unificación de Booch, Rumbaugh y Jacobson, y la adopción de UML por el OMG en 1997.
  - **La plantilla de una clase en UML**: una caja de tres partes (nombre, atributos y métodos), con la forma `visibilidad nombre : tipo` para los atributos y `visibilidad nombre(parámetros) : tipo` para los métodos. Visibilidad: `+` público, `-` privado (`#` protegido y `~` paquete existen, pero no se usan en el curso).
  - **De UML a Python**: el nombre va en `class`; los atributos nacen dentro de `__init__` con `self`; cada método va en su `def` y recibe `self` como primer parámetro, aunque en UML no aparece. El constructor se escribe `__init__`, pero se usa con el nombre de la clase: `r1 = Rectangulo(3.0, 4.0)`.
- **Ejemplo 1, `Rectangulo`** (diapositivas 26-34): del enunciado al UML (los tipos se deciden al diseñar), del UML a Python, instanciar un objeto y usarlo, y probar con dos rectángulos. `r1 is r3` da `False` aunque tengan los mismos valores: son dos objetos distintos.
  - **El problema de los atributos públicos**: `r1.base = -5.0` se acepta sin control y el área sale `-20.0`.
  - **La versión mejorada**: atributos privados (`self.__base`), *getters* para consultar y *setters* para cambiar validando. `set_base` y `set_altura` devuelven `True` si aceptaron el valor y `False` si lo rechazaron (en la industria se lanzaría una excepción, que el curso no ve). Pruebas con un caso típico (5.0), uno límite (0.0) y uno especial (-5.0).
  - **`__` no es un candado**: Python cambia el nombre del atributo por dentro (`_Rectangulo__base`), así que `r1.__base = -5.0` desde afuera no da error, pero crea otro atributo y la base verdadera no cambia. En Java, `private` sí es un candado.
- **Ejemplo 2, `Ventilador`** (diapositivas 35-39): constantes de clase (`LENTO`, `MEDIO` y `RAPIDO`, subrayadas en UML porque son de la clase y no de cada objeto), valores por defecto en el constructor (en Java se escribirían varios constructores; en Python basta uno), un método sin tipo de retorno que cambia el estado y devuelve `None` (`print(v2.encender())` muestra `None`), y `__str__`, que da el texto que muestran `print(v2)` y `str(v2)`. Con `str()` se puede probar con `assert`. No hay `set_radio`: no todo atributo necesita un *setter*.
- **Ejemplo 3, `Celular`** (diapositivas 40-41): "Hágalo usted mismo" a partir del diagrama UML, con su solución. Aquí los *setters* no validan. El reto: que `set_precio` rechace precios menores o iguales a 0 y devuelva `True` o `False`, lo que cambia su línea en el UML a `+ set_precio(precio: float) : bool`.
- **Ejemplo 4, `Titular` y `CuentaBancaria`** (diapositivas 42-48): dos clases, donde un atributo de la cuenta es un objeto `Titular` y `transferir` recibe otra cuenta como parámetro y usa `retirar` y `depositar`. No hay `set_saldo`: el saldo solo cambia con depositar, retirar y transferir. La **asociación** se dibuja con una flecha de la cuenta al titular (la cuenta conoce a su titular; el titular no sabe qué cuentas tiene), con su multiplicidad; diseñar el UML de programas grandes es tema de Ingeniería de Software. Las pruebas recorren el escenario del enunciado (Homero le transfiere 15000.0 a Marge, Marge intenta transferir más de lo que tiene) y revisan los dos saldos en cada caso.
- **Ejemplo 5, un arreglo de cuentas** (diapositivas 49-51): `cuentas = [None] * 3` con las cuentas de Homero, Marge y el señor Burns. La posición del mayor saldo es la búsqueda de siempre, comparando `cuentas[i].get_saldo()`. Para dar un bono no se reasigna la casilla: se le pide al objeto que cambie, con `cuentas[i].depositar(10000.0)`.
- **El sistema crece: la clase `Banco`** (diapositivas 52-59): el arreglo que vivía suelto en el programa pasa a ser un atributo, `cuentas : CuentaBancaria[*]`, con su cupo y su `cantidad`. Como el banco crea sus cuentas en `abrir_cuenta`, la relación es de **composición** (◆); entre la cuenta y el titular sigue habiendo una asociación. La precisión sobre composición y agregación sigue a Fowler.
  - Métodos: `abrir_cuenta` (devuelve `False` si no hay cupo), `posicion_mayor_saldo(inicio=0)` (sirve para buscar el mayor y para ordenar), `ordenar_por_saldo` (selección de mayor a menor con un solo intercambio por paso, porque se mueve la cuenta completa) y `dar_bono`. Los recorridos van hasta `cantidad`, no hasta `len()`, porque las casillas libres siguen en `None`.
  - Pruebas: las del Ejemplo 5, más ordenar, llenar el cupo y rechazar una cuenta cuando el banco está lleno.
  - **¿Por qué POO?**: el tablero de incomodidades con el banco. Tres incomodidades quedan resueltas (la cuenta existe, se intercambia una cuenta y `cantidad` vive dentro de `Banco`) y agregar un dato solo cambia `Titular`; la de un método por cada criterio de orden sigue igual.
- **Cierre** (diapositivas 60-63):
  - **El bloque 2 en UML**: `Estudiante` y `Curso`, con el mismo problema y el mismo menú de la clase 12. `Curso` se parece a `Banco` (un arreglo de objetos con cupo y cantidad), pero `agregar_estudiante` recibe un estudiante que ya existe.
  - **Composición y agregación**: se distinguen mirando quién crea el objeto. `abrir_cuenta` crea la cuenta adentro: composición (◆). `agregar_estudiante` guarda un estudiante creado afuera: agregación (◇).
  - **Errores típicos**: olvidar `self`, escribir `print(r1.calcular_area)` sin paréntesis, comparar objetos con `==`, definir dos métodos con el mismo nombre (el segundo reemplaza al primero) y escribir `r1.__base` desde afuera. Los más peligrosos son los que no dan error.
  - **Resumen**: cada concepto con su forma en UML y en Python.
- **Referencias** (diapositivas 64-66) y cierre (diapositiva 67): la *Guía Teórica 02* de Mera Banguero, [CS50P, Lecture 8](https://cs50.harvard.edu/python/weeks/8/), la [documentación de Python sobre variables privadas](https://docs.python.org/es/3.11/tutorial/classes.html#private-variables), [Python Tutor](https://pythontutor.com) (los enlaces de simulación de las diapositivas se ejecutan allí), los libros de Liang, Gaddis, Bloch y Meyer, el [estándar UML 2.5.1](https://www.omg.org/spec/UML/2.5.1), [Kobryn (1999)](https://cacm.acm.org/research/uml-2001), el curso [Inf2-SEPP](https://opencourse.inf.ed.ac.uk/inf2-sepp) de Edinburgh, [Fowler (2003)](https://martinfowler.com/bliki/AggregationAndComposition.html) y el [tutorial de Chua Hock Chuan](https://www3.ntu.edu.sg/home/ehchua/programming/java/J3b_OOPInheritancePolymorphism.html).

## Recursos

| Archivo | Descripción |
|---|---|
| [clase-13.pdf](clase-13.pdf) | Diapositivas completas del tema 13, en PDF. |
| [clase-13.pptx](clase-13.pptx) | Diapositivas completas del tema 13, editable (PowerPoint, 67 diapositivas). |
| [diagramas/](diagramas/) | Fuentes `.drawio` de los diagramas (ver la tabla siguiente). |
| [images/](images/) | Exportación en `.png` de los diagramas de `diagramas/`. |
| [codigo/](codigo/) | Scripts de los ejemplos (ver [Código de ejemplo](#código-de-ejemplo)). Su [README](codigo/README.md) reúne el **enunciado** de cada ejemplo con los archivos que lo resuelven. |
| [app_curso/](app_curso/README.md) | El programa del curso resuelto con arreglos paralelos y con las clases `Estudiante` y `Curso` (el bloque 2 implementado), con una página de comparación. |
| [app_piedra-papel-tijera/](app_piedra-papel-tijera/README.md) | El juego de piedra, papel o tijera resuelto con funciones y con las clases `Jugador`, `Ronda` y `Partida`, con una página de comparación. |
| [app_transporte/](app_transporte/README.md) | Una plataforma de transporte con cinco clases relacionadas (`Punto`, `Cliente`, `Conductor`, `Viaje`, `Plataforma`), con menú y manual de usuario. El diseño se explica en el notebook [De una clase a varias](../sesion_magistral-32/notebooks/aplicacion_transporte.ipynb). |

> [!TIP]
> El código de cada ejemplo está completo y probado en `codigo/`. Para copiar código, conviene tomarlo de los scripts y no de las diapositivas, donde las líneas largas se parten para que quepan.

### Diagramas

Cada fuente de `diagramas/` tiene su imagen, con el mismo nombre, en `images/`, salvo donde se indica.

| Fuente (`diagramas/`) | Imagen | Contenido |
|---|---|---|
| [arreglo_parcial.drawio](diagramas/arreglo_parcial.drawio) | [arreglo_parcial.png](images/arreglo_parcial.png) | Repaso: los tres vectores de tamaño 10 con 4 casillas ocupadas y `cantidad = 4`. Es el mismo diagrama de la clase 12. |
| [intercambio_paralelo_sin_codigo.drawio](diagramas/intercambio_paralelo_sin_codigo.drawio) | [intercambio_paralelo_sin_codigo.png](images/intercambio_paralelo_sin_codigo.png) | Repaso: un estudiante se intercambia en los tres vectores. Es el mismo diagrama de la clase 12. |
| [tablero_incomodidades.drawio](diagramas/tablero_incomodidades.drawio) | [preview_1_inicio.png](images/preview_1_inicio.png) | El tablero de incomodidades (con arreglos paralelos / con objetos / estado). La fuente tiene seis páginas, una por cada momento en que se actualiza el tablero; la imagen es la primera página, con todo "por comprobar". |
| [paradigma_estructurada.drawio](diagramas/paradigma_estructurada.drawio) | [paradigma_estructurada.png](images/paradigma_estructurada.png) | El promedio en programación estructurada: los datos sueltos y la operación aparte. No se usa en las diapositivas. |
| [paradigma_estructurada_sin_leyenda.drawio](diagramas/paradigma_estructurada_sin_leyenda.drawio) | [paradigma_estructurada_sin_leyenda.png](images/paradigma_estructurada_sin_leyenda.png) | El mismo diagrama, sin la leyenda. |
| [paradigma_poo.drawio](diagramas/paradigma_poo.drawio) | [paradigma_poo.png](images/paradigma_poo.png) | El promedio en POO: el objeto `curso` tiene sus notas y sabe calcular su promedio. No se usa en las diapositivas. |
| [paradigma_poo_sin_leyenda.drawio](diagramas/paradigma_poo_sin_leyenda.drawio) | [paradigma_poo_sin_leyenda.png](images/paradigma_poo_sin_leyenda.png) | El mismo diagrama, sin la leyenda. |
| [plano_casas.drawio](diagramas/plano_casas.drawio) | [plano_casas.png](images/plano_casas.png) | Un plano (la clase `Casa`) y tres casas (los objetos), cada una con su color y su dirección. |
| [objeto_casa.drawio](diagramas/objeto_casa.drawio) | [objeto_casa.png](images/objeto_casa.png) | Estado, comportamiento e identidad de una casa; dos casas con el mismo estado y distinta dirección. |
| [estudiante_objetos.drawio](diagramas/estudiante_objetos.drawio) | [estudiante_objetos.png](images/estudiante_objetos.png) | La clase `Estudiante` y dos objetos, `lisa` y `bart`, con sus propios valores. |
| [encapsulamiento.drawio](diagramas/encapsulamiento.drawio) | [encapsulamiento.png](images/encapsulamiento.png) | Los datos privados en el centro y los métodos públicos alrededor; el código de afuera solo usa los métodos. |
| [linea_tiempo_uml.drawio](diagramas/linea_tiempo_uml.drawio) | [linea_tiempo_uml.png](images/linea_tiempo_uml.png) | Línea de tiempo de UML, de 1989 a 1997. |
| [plantilla_uml.drawio](diagramas/plantilla_uml.drawio) | [plantilla_uml.png](images/plantilla_uml.png) | La caja de tres partes de una clase en UML: nombre, atributos y métodos. |
| [uml_a_python.drawio](diagramas/uml_a_python.drawio) | [uml_a_python.png](images/uml_a_python.png) | Cada parte del diagrama UML y su lugar en el código Python. |
| [figura_rectangulo.drawio](diagramas/figura_rectangulo.drawio) | [figura_rectangulo.png](images/figura_rectangulo.png) | El rectángulo con su base, su altura y las fórmulas del área y el perímetro. |
| [uml_rectangulo.drawio](diagramas/uml_rectangulo.drawio) | [uml_rectangulo.png](images/uml_rectangulo.png) | UML de `Rectangulo` con atributos públicos, con notas sobre cómo se escribe cada parte. No se usa en las diapositivas. |
| [uml_rectangulo2.drawio](diagramas/uml_rectangulo2.drawio) | [uml_rectangulo2.png](images/uml_rectangulo2.png) | El mismo UML, sin las notas. |
| [instanciar_rectangulo.drawio](diagramas/instanciar_rectangulo.drawio) | [instanciar_rectangulo.png](images/instanciar_rectangulo.png) | Qué pasa al ejecutar `r1 = Rectangulo(3.0, 4.0)`: la clase, `self` durante `__init__` y el objeto que queda en `r1`. |
| [rectangulo_tres_objetos.drawio](diagramas/rectangulo_tres_objetos.drawio) | [rectangulo_tres_objetos.png](images/rectangulo_tres_objetos.png) | Tres objetos de la misma clase: `r1` y `r3` con los mismos valores, `r2` con otros. |
| [uml_rectangulo_privado.drawio](diagramas/uml_rectangulo_privado.drawio) | [uml_rectangulo_privado.png](images/uml_rectangulo_privado.png) | UML de `Rectangulo` con atributos privados, *getters* y *setters*. |
| [uml_ventilador.drawio](diagramas/uml_ventilador.drawio) | [uml_ventilador.png](images/uml_ventilador.png) | UML de `Ventilador`, con las constantes subrayadas y los valores por defecto del constructor. |
| [uml_celular.drawio](diagramas/uml_celular.drawio) | [uml_celular.png](images/uml_celular.png) | UML de `Celular`, para el ejercicio "Hágalo usted mismo". |
| [uml_titular.drawio](diagramas/uml_titular.drawio) | [uml_titular.png](images/uml_titular.png) | UML de `Titular`. |
| [uml_cuenta.drawio](diagramas/uml_cuenta.drawio) | [uml_cuenta.png](images/uml_cuenta.png) | UML de `CuentaBancaria`; los tipos que son clases van en negrita. |
| [uml_cuenta_titular.drawio](diagramas/uml_cuenta_titular.drawio) | [uml_cuenta_titular.png](images/uml_cuenta_titular.png) | La asociación entre `CuentaBancaria` y `Titular`, con su multiplicidad. |
| [arreglo_cuentas.drawio](diagramas/arreglo_cuentas.drawio) | [arreglo_cuentas.png](images/arreglo_cuentas.png) | Un arreglo de tres casillas, cada una con una cuenta que guarda su titular. |
| [uml_banco.drawio](diagramas/uml_banco.drawio) | [uml_banco.png](images/uml_banco.png) | `Banco`, `CuentaBancaria` y `Titular`: composición entre el banco y sus cuentas, asociación entre la cuenta y el titular. |
| [uml_banco_clase.drawio](diagramas/uml_banco_clase.drawio) | [uml_banco_clase.png](images/uml_banco_clase.png) | UML de `Banco`, con el atributo `cuentas : CuentaBancaria[*]`. |
| [uml_estudiante_curso.drawio](diagramas/uml_estudiante_curso.drawio) | [uml_estudiante_curso.png](images/uml_estudiante_curso.png) | El bloque 2: UML de `Estudiante` y de `Curso`. |
| [uml_composicion_banco.drawio](diagramas/uml_composicion_banco.drawio) | [uml_composicion_banco.png](images/uml_composicion_banco.png) | Composición: `abrir_cuenta` crea la cuenta dentro del banco. |
| [uml_agregacion_curso.drawio](diagramas/uml_agregacion_curso.drawio) | [uml_agregacion_curso.png](images/uml_agregacion_curso.png) | Agregación: `agregar_estudiante` guarda un estudiante creado afuera. |

### Código de ejemplo

| Código | Descripción |
|---|---|
| [codigo/ej1_rectangulo.py](codigo/ej1_rectangulo.py) | `Rectangulo` con atributos públicos. Imprime `False` (`r1 is r3`), `Rectangulo: todas las pruebas pasaron`, y luego `-20.0` y `-2.0` después de `r1.base = -5.0`. |
| [codigo/ej1_rectangulo_privado.py](codigo/ej1_rectangulo_privado.py) | `Rectangulo` con atributos privados, *getters* y *setters* que validan. Imprime `Rectangulo: todas las pruebas pasaron` y, para mostrar que `__` cambia el nombre, `3.0`, `12.0`, `-5.0` y `3.0`. |
| [codigo/ej2_ventilador.py](codigo/ej2_ventilador.py) | `Ventilador` con constantes de clase, valores por defecto y `__str__`. Imprime `3 10.0 amarillo True`, `1 5.0 azul False`, las descripciones antes y después de encenderlo (con `None` en medio) y `Ventilador: todas las pruebas pasaron`. |
| [codigo/ej3_celular.py](codigo/ej3_celular.py) | `Celular`, con el reto del `set_precio` que devuelve `bool` en un comentario → `Celular: todas las pruebas pasaron`. |
| [codigo/ej4_cuenta_titular.py](codigo/ej4_cuenta_titular.py) | `Titular` y `CuentaBancaria`. Imprime `Homero Simpson: $30000.0`, `Marge Simpson: $0.0`, `True`, `False`, los dos saldos en `$15000.0` y `CuentaBancaria: todas las pruebas pasaron`. Tiene la guarda `if __name__ == "__main__":` porque el Ejemplo 5 importa sus clases. |
| [codigo/ej5_arreglo_cuentas.py](codigo/ej5_arreglo_cuentas.py) | Un arreglo de tres cuentas. Imprime `2`, `Señor Burns: $1000000.0` y las tres cuentas después del bono. Importa de `ej4_cuenta_titular.py`, así que se ejecuta desde la carpeta `codigo/`. |
| [codigo/ej6_banco.py](codigo/ej6_banco.py) | La clase `Banco`, con `Titular`, `CuentaBancaria` y la función `intercambiar` en el mismo archivo. Imprime lo mismo que el Ejemplo 5, las cuentas ordenadas de mayor a menor saldo y `Banco: todas las pruebas pasaron`. |

> [!Important]
> Se usó IA generativa para redactar y organizar este contenido a partir de las diapositivas de la clase. El docente revisó y validó la versión final.
