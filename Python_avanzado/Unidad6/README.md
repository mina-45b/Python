# Introducción a la programación avanzada

### UNIDAD 6

docs.python.org/3/howto/

### Set

Los conjuntos en Python, en mátematicas, un conjunto es una colección de valores sin duplicados. En Python, este concepto se materialzia como un tipo de dato real. 

docs.python.org/3/libreary/stdtypes.html#set

### Global

En algunos lenguajes, existe la noción de variable globales, las cuales pueden ser definidas fuera de funciones y accedidas desde cualquier parte del programa. Sin embargo, en Python, estas variables pueden comportarse como globarles en el contexto de un módulo, pero es esencial comprender sus limitaciones.

Se recomiendo el uso de las variables globales con moderación para evitar problemas de poca legibilidad y comprensión

### constantes

En algunos lenguajes de programación podemos definir variables que actúan como constantes. Estas variables, una vez que les asignamos un valor, no pueden cambiar. Esto proporciona una capa de defensa, evitando modificaciones accidentales.

En Python, no hay una característica específica que  haga una variable sea constante. Es una cuestión de convención, donde suelen escribir en mayústulas las varibales que deben tratarse como constantes. Sin embargo, el lenguaje no impide cambiar esos valores.

### Type hints, mypy

En Python, un lenguja tipado dinámicamente, las variables no están fuertemente tipadas. Esto significa que no es necesario especificar el tipo de variable al declararla, permitiendo una flexibilidad considerble.

docs.python.org/3/library/typing.html

Las sugerencias de tipo, introducidas con Type Hints, permiten al programador indicar el tipo esperado de una variable o función. 

Mypy es una herramienta popular que verifica si nuestro código se adhiere a estas sugerencias, ayudándonos a identificar posibles errores antes de la ejecución.

mypy.readthedocs.io

### Docstrings

Cadenas de documentación
peps.python.org/pep-0257/

### argparse

A menudo queremos interactuar con el usuario de diversas maneras. Una forma común es a trabés de la línea de comandos, donde el usuario puede proporcionar información adicional al ejecutar el programa. En lugar de depender únicamente del prompr, argparse nos ofrece una forma más organizada de manjear estos argumentos de línea de comandos.

dosc.python.org/3/library/argparse.html

### Unpacking

Desempaquetar es una técnica en Python que nos permite trabajar con estructuras de datos, como listas o diccionarios, de manera más flexible y sencilla. Nos ayuda a dividir valores almacenados en una estructura en variables individuales, facilitando el manejo de datos complejos.

Para desempaquetar listas usamos *

Para desempaquetar diccionarios usarmos **

Funciones como Argumentos Variables: Podemos crear funciones que aceptan un número variable de argumentos poscionales y con nombre utilizando *args y **kwargs

### Map

Una herramienta valiosa que Python nos ofrece es map. Esta función nos permite aplicar otra función a cada elemento de una secuencia, como una lista.
Imagina forzar a mayúsculas una lista de palabras, para ello podemos utilizar map y aplicar la función upper a cada palabra de manera eficiente.

docs.python.org/3/library/functions.html#map

- Comprensión de lista: es una forma concisa y elegante de construir listas en Python sin necesidad de usar bucles tradicionales o la función append. Permite crear listas sobre la marcha utilizando una única línea de código, lo que a menudo resulta en un códifo más limpio y legible.

- Comprensión de diccionarios

### Filter

docs.python.org/3/library/functions.html#filter

### enumerate()
Python nos ofrece la función incorporada enumerate(). Esta función nos permite iterar sobre una secuencia y obtener tanto el índice como el valor de cada elemento de manera más eficiente.

docs.python.org/3/library/functions.html#enumerate

> enumerate(iterable, start=0)

Generators: El uso de generadores en Python, es una técnica que nos permite generar y devolver valores de manera eficiente, uno a la vez, sin cargar la memoria.

yiel: devuelve un iterador