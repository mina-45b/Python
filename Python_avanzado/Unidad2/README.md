Introducción a la programación avanzada

UNIDAD 2

Unitest (pruebas unitarias): son una práctica fundamental en el desarrollo de software. Consiste en escribir código adicional para verificar que nuestras funciones y programas resuelvan los problemas de manera correcta.

assert: palabra clave, que permite hace audaces afirmaciones sobre la veracidad de una expresión booleana. Si la afirmación es cierta, todo continua sin porblemas; sin embargo, si la afirmación resulta falsa, Python mostrará un error en la pantalla.

>[!IMPORTAN]
>Al momento de realizar pruebas unitarias, debemos pensar cuales son aquellos casos inusuales que podrían darnos errores para poder incluirlos en las pruebas, además de incluir casos comunes.

Pytest: es un programa de terceros que autiomatiza las pruebas de código, siempre y cuando escribas las pruebas correspondientes.

Lo interesante es que adopta algunas convenciones, lo que significa que no necesitas escribir manualmente tantas líneas de código; hace parte del trabajo por ti.

instalación: pip install pytest
documentación: docs.pytest.org
uso: pyteste nombre_archivo.py

Una estrategia que se puede implementar a la hora de crear nuestras pruebas es dividirlas en funciones con categerías específicas.

Ejem. -> Para el programa: def squared(n):
                                return n * n
Proponemos dividir las pruebas en Números positivos - Números negativos - Cero.

Consideraciones en las pruebas unitarias:

- Destacamos la importancia de no probar efectos secundatios directamente (como una impresión), ya que las pruebas deben centrarse en valores de retorno.

- Se sugiere la simplificacion de las pruebas para grantizar su comprensió y eficiencia.

Colecciones de test:  

Imaginemos que no estamos limitados a una sola prueba, sino que queremos estructurar nuestras pruebas en una carpeta llamada "test". Varios frameworks, como pytest, admiten este enfoque, proporcionándonos flexibilidad y organización.

>[!NOTE]
>Para que pytest reconozca la carpeta como un paquete, crearemos un archivo "init.py" dentro de la carpeta.

Ejem. -> test/__init__.py