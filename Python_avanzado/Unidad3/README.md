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

CSV (Valores Separados por Coma): permiten organizar y manipular fácilmente los datos.

En python utilizamos la función sorted() con un parámetro adcional llamado key, que nos permitirá especificar la clave según la cual deseamos ordenar.

Las funciones lambda son funciones anónimas sin nombre que se utilizan generalmente para operaciones simples y se definen en el momento en que se necesitan.

Lambda como función anónima:
- A diferencia de def, no tiene un nombre asociado.
- se usa directamente donde se necesita, en este caso, como la clave para sorted().
- Puedes usar lambda tantas veces como necesites en contextos donde una función anónima es suficiente.


Biblioteca csv: esta herramienta nos permite leer y escribir archivos CSV de manera más eficiente, evitando problemas con las comas y otros caracteres especiales.
>import csv

documentación: docs.python.org/3/library/csv.html

Consideraciones sobre modificaciones en Archivos:
- Es posible modificar el archivo mientras lo leemos, pero debemos tener en cuenta que el archivo es secuencial.
- Se debe mantener un registro de la posición en el archivo para realizar cambios eficientemente.
- Podemos solicitar al usuario ingresar datos para escribir en el archivo.
- La versatilidad del csv.reader nos permite trabajar con diversos datos.

csv.DictReader: nos permite acceder a los datos como diccionarios en lugar de listas. Esto significa que podemos referenciar las columnas por sus nombres, lo cual es más intuitivo y menos propenso a errores.


PIL Librería: es una biblioteca que facilita la navegación y manipulación de archivos de image.

Tutorial: pillow.readthdocs.io

