![Built with AI](https://img.shields.io/badge/Built%20with-AI-blue.svg)

# Administración de notas de un curso

## Qué hace

> Un curso admite máximo `N = 10` estudiantes. De cada uno se guarda su Id (texto), su nombre y su nota. Se necesita un programa con menú para agregar, eliminar, actualizar la nota, buscar, listar y ordenar (por nota o por nombre).

Es el programa integrador de la [clase 12](../../../README.md) (diapositivas 44 a 57). Los estudiantes se guardan en tres **arreglos paralelos** (`ids`, `nombres` y `notas`) **parcialmente llenos**: `cantidad` dice cuántas casillas están ocupadas. Para ordenar se usa la selección, y cada intercambio mueve al estudiante completo en los tres arreglos.

Para verlo construido paso a paso: notebook [Administración de un curso con arreglos paralelos](../../../../13/teoria/app_curso/notebooks/curso_estructurado.ipynb). El mismo problema resuelto con objetos está en [app_curso](../../../../13/teoria/app_curso/README.md) (clase 13).

## Los archivos

```
📁 curso/
   📄 curso.py — las funciones del curso (importa ordenamientos.py)
   📄 ordenamientos.py — copia del ordenamientos.py de la clase
   📄 test_curso.py — las pruebas con assert
   📄 main.py — el programa con menú
```

| Archivo | Contenido |
|---|---|
| [curso.py](curso.py) | `buscar_id`, `agregar_estudiante`, `eliminar_estudiante`, `actualizar_nota`, `mostrar_listado`, `intercambiar_estudiantes`, `posicion_mayor_nota`, `ordenar_por_nota`, `posicion_menor_nombre` y `ordenar_por_nombre` |
| [ordenamientos.py](ordenamientos.py) | Una copia de [../ordenamientos.py](../ordenamientos.py): `curso.py` usa su función `intercambiar`, y Python solo encuentra el módulo si está en la misma carpeta. Si se cambia uno, hay que cambiar el otro |
| [test_curso.py](test_curso.py) | Pruebas de cada función, incluidos un Id repetido, el cupo lleno y que cada estudiante conserve sus datos al ordenar |
| [main.py](main.py) | El menú. Empieza con cuatro estudiantes inscritos: Ana, Beto, Carla y Dario |

## Cómo ejecutarlo

```
cd clases/12/teoria/codigo/curso
python test_curso.py
python main.py
```

## Salida esperada

Las pruebas:

```
Pruebas de curso: todas pasaron
```

Una sesión con el menú: se lista el curso, se agrega a Elena, se intenta agregar un Id repetido, se ordena por nota, se busca un estudiante, se intenta eliminar un Id que no existe y se sale. Para abreviar, el menú se muestra completo solo la primera vez:

```
=== Administración del curso ===
1. Agregar estudiante
2. Eliminar estudiante
3. Actualizar nota
4. Buscar estudiante
5. Listar curso
6. Ordenar por nota
7. Ordenar por nombre
0. Salir
Opción: 5
Id 	 Nombre 	 Nota
000 	 Ana 	 3.0
123 	 Beto 	 4.5
987 	 Carla 	 2.0
007 	 Dario 	 4.0
...
Opción: 1
Id: 555
Nombre: Elena
Nota: 3.5
Estudiante agregado.
...
Opción: 1
Id: 123
Nombre: Otro
Nota: 2.0
No se pudo agregar: el curso está lleno o el Id ya existe.
...
Opción: 6
Id 	 Nombre 	 Nota
123 	 Beto 	 4.5
007 	 Dario 	 4.0
555 	 Elena 	 3.5
000 	 Ana 	 3.0
987 	 Carla 	 2.0
...
Opción: 4
Id a buscar: 007
007 Dario 4.0
...
Opción: 2
Id a eliminar: 999
No existe un estudiante con ese Id.
...
Opción: 0
Hasta luego.
```

Al ordenar, cada nombre sigue con su Id y su nota: el estudiante se mueve completo.

## Si algo falla

| Lo que pasa | Por qué | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: No module named 'ordenamientos'` | Se ejecutó desde otra carpeta, o falta la copia de `ordenamientos.py` | Entrar a la carpeta `curso` antes de ejecutar |
| No se encuentra el Id `7` | Los Id son **textos**: `007` no es lo mismo que `7` | Escribir el Id tal como está en el listado |
| Un nombre en minúscula o con tilde queda en otro lugar al ordenar por nombre | La comparación de textos distingue mayúsculas y tildes (`"ana" < "Beto"` es `False`) | Escribir los nombres con mayúscula inicial y sin tildes, como supone `posicion_menor_nombre` |
| Al cerrar el programa, los cambios se pierden | Los arreglos viven en la memoria | Es el problema que resuelve la [clase 15](../../../../15/README.md) con archivos |

> [!Important]
> Se usó IA generativa para redactar esta guía a partir del código de la clase. Las salidas son de ejecuciones reales. El docente revisa y valida la versión final.
