Introducción a la programación avanzada

UNIDAD 4

Expresión regular: también conocida como regexes, es un patrón utilizado comúnmente en programación para comparar datos.

re: es una biblioteca que nos permite definir y validar patrones con mayor precisión. Las expresiones regulares ofrecen una manera mas potente y flexible de trabajar con patrones.

documentación: docs.python.org/3/library/re.html

Con la librería re, podemos:
- Definir patrones de búsqueda, como el formato de una dirección de correo electrónico.
- Verificar la validez de una entrada de usuario frente a un patrón definido.
- Manipular y extraer información de las cadenas de texto según los patrones definidos.

Búsqueda:
re.search(pattern, string, flags=0)

- pattern: patron de búsqueda.
- string: cadena real dek usuario.
- flags: banderas, parametro para modificar el parametro de la función.

Símbolos especiales de patron:
- Punto(.): cualquier carácter excepto una nueva línea.
- Asperisco(*): cero o más repeticiones del elemento anterior.
- Más(+): una o más repeticiones del elemento anterior.
- Interrogación(?): cero o una repetición del elemento anterior.
- Llaves({m}, {m,n}): un número exacto(m) o un rango (m a n) de repeticiones.




