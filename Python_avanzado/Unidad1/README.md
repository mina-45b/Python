Introducción a la programación avanzada

UNIDAD 1

Biblioteca: son conjuntos de código preescrito que podemos utilizar en nuestros propios programas.

Módulos: son una parte esencial de las bibliotecas, contienen funciones y características específicas
que podemos incorporar en nuestros proyectos.

La principal ventaja de las bibliotecas y Módulos es la reutilización de código.

Bibliotecas de Python:

- random
- statistics
- sys

import: para utilizar las funciones de un módulo en nuestros propios programas, necesitamos
usar la palabra clave 'import' seguida del nombre del módulo.

ramdon:
radom.choice(seq)
random.randint(a,b)
radom.shuffle(x)

from: se utiliza al importar funciones de un módilo. Nos ser más específicos y seleccionar solo lo que necesitamos.

argumento de líneas de comandos (command-line argumets): Nos permite interactuar con nuestro porgrama directamente desde la terminal.

argv: vector de argumentos.

sys:
sys.argv: Al ejecutar un programa, sys.argv nos propociona una lista de argumentos.
sys.exit

IndexError: list index out of range: Este error sucede cuando intentamos acceder a un elemento en una posición que no existe 
dentro de la lista. 

"" <- Escribimos entre comillas para que un fragmente se cuente como un solo parámetro

Slices: es un subconjunto de una estructura de datos, como una lista.
En Python, podemos tomar slices de listas utilizando una sintaxis fácil. Al añadir
corchetes al final del nombre de la lista, especificamos el inicio y el final del subconjunto
que queremos conservar.

Puedes cortar o "slicing" desde cualquier punto, incluso desde el final.
Utiliza un número negativo para contar en dirección opuesta desde el finalde la lista.

Ejem. -> for arg in sys.argv[1:-1]

packages: es como un regalo lleno de funciones y capacidades adicionales que otros programadores han creado para nosotros.
Es una biblioteca de terceros que se puede instalar para acceder a estas funcionalidades.

pipy.org: sitio web que contine paquetes que podeos explorar, descargas e instalar.

cowsay: es un paquete en python que una vaca hable.

[!IMPORTANT]
En entornos de Linux, no se pueden instalar los paquetes directamente, una alternativa es crear un entorno virtual aislado para poder instalarlo ahí directamente.

>[!IMPORTANT]
> Key information users need to know to achieve their goal.