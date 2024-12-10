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