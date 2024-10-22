Introducción a la programación avanzada

UNIDAD 3

open(): 

Es una función que permite abrir archivos de lectura, escritura o ambos.
Devuelve un "manejador de archivo" que proporciona acceso al archivo para realizar operaciones como leer, escribir y cerrar archivos.

Documentación: docs.python.org/3/library/functions.html#open


- r: Abre el fichero en modo lectura.
- r+: Si quieres leer y escribir en el fichero.
- w: Para sobreescribir el contenido.
- a: Para añadir al final del fichero en el caso de que ya exista.

>[!NOTE]
> r es el valor predeterminado de open, por tanto para leer un archivo podremos poner simplemente open("file.txt")

Ejem. -> file = open("names.txt", "w")

Ejem. -> file = open("Python_avanzado/Unidad3/names.txt", "a")

Para abrir un archivo, solo necesitas proporcionar el nombre del archivo como primer argumento. Opcionalmente, puedes especificar el modo de apertura, como archivo para lectura o 'w' para escritura.

with: se utiliza para simplificar la apertura y cierre de archivos en Python, asegurando que los recursos se manejen de manera adecuada.

readlines(): es un método de open() que permite leer todas las líneas de un archivoy devolverlo en una lista.

rstrip(): método que permite eliminar los espacioes en blanco, como los saltos de líneas.

sorted(): Función que nos permite ordenar elementos de manera ascendente o descendente.

sorted(iterable, /, *, key=None, reverse=False)

- iterable: es algo sobre lo que se puede iterar o hacer un bucle.
- key: especifica una clave para ordenar.
- reverse: por defecto es False, si se cambia a True, invertirá el orden de la clasificación.

>[!NOTE]
>Utilizar strip para eliminar espacios en blanco al final de las líneas es útil, pero se debe considerar si realmente es necesario. A veces, otras funciones como readlines pueden manejarlo automáticamente.
