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
- json

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

>[!IMPORTANT]
>En entornos de Linux, no se pueden instalar los paquetes directamente, una alternativa es crear un entorno virtual aislado para poder instalarlo ahí directamente.

API (Interfaz de Programación de Aplicaciones): es una interfaz que permite a diferentes aplicaciones comunicarse entre sí. 

En el contexto de la programación, a menudo se refiere a servicios de terceros con los que podemos interactuar mediante código para obtener o enviar datos.

Request: python ofrece el paquete 'requests', que nos permite realizar solicitudes a servidores web como si fuéramos navegadores.

Documentación de la libreraría: https://pypi.org/project/requests/

Instalar: pip install requests

JSON (JavaScropt Object Notation): muchas APIs devuelven datos en formato JSON, un lenguaje agnóstico para el intercambio de datos entre computadoras. Es un formato basado en texto que utiliza llaves, corchetes y dos puntos para estructurar la información.

Documentación de la biblioteca: docs.python.org/3/library/json.html

Ejem. -> {
            "resultCount":1,
            "results": [
            {"wrapperType":"track", "kind":"song", "artistId":115234, "collectionId":1440878798, "trackId":1440879325}
            ]
        }

ITUNES:

Ejem. -> URL: https://itunes.apple.com/search?entity=song&limit=1&term=weezer

Librerias personalizadas:

En Python, tenemos la capcidad de construir nuestras propias bibliotecas o módulo. Esto no solo permite optimizar nuestro código, sino también compartir nuestras soluciones con otros programadores.

>[!IMPORTANT]
>Cuando crearmos una propia librería debemos tener en cuenta que si utilizamos un método que se llamé por defecto (ejem. main()), este se seguirá ejecutando incluso cuando la importemos.

Como usar nuestras librerias: 

if __name__ == "__main__":
    main()

__name__: es una variable  espacial cuyo valor es automático establecido por python, para ser main cuando ejecutas un archivo desde la línea de comandos. 

>En Python, __name__ es una variable especial que el intérprete asigna al nombre del módulo de Python . Si el módulo se invoca como un script, la cadena '__main__' se asignará automáticamente a la variable especial __name__.

Estilo: se refiere a cómo presentamos nuestro código. En python, hay estándares conocidos como PEP 8 que establecen reglas sobre cómo formatear y organizar el código. 

La idea principal es que un código bien escrito no solo sea funcional y bien diseñado, sino también fácil de ller y mantener.  

documentación: peps.python.org/pep-0008

Principios clave del estilo en Python:

- Sangría consistente: se utiliza una sangría de cuatro espacios para estructurar el código. Esto ayuda a que sea más legible.
- Longitud máxima de línea: Limitamos la longitud de las líneas para mejorar la legibilidad. PEPE 8 sugiere no superar cierto número de caracteres a la derecha de la pantalla.
- Líneas en blanco: El uso adecuado de líneas en blanco entre bloques de código y comentarios mejora la legibilidad y oragnización del código.
- Importaciones ordenadas: PEP 8 prescribe cómo y dónde colocar las importaciones, manteniendo un orden específico. 

Herramientas para mantener el estilo: 

- pylint -> pip install pylint - documentación: pycodestyle.pycqa.org
- pycodestyle -> documentación: pycodestyle.pycqa.org
- black -> pip install black - documentación: black.readthedocs.io
    Ejem. Formatear archivo: black name-archivo.py

Importancia del estilo: un código bien formateado no solo es estéticamente agradable. También facilita la detección y corrección de errores. La coherencia en el estilo es clave, ya que ayuda a comprender y mantener el código a medida que evoluciona.
