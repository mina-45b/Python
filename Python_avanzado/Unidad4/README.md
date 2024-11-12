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

- Signo de intercalación (^): Indica el inicio de la cadena.
- Signo dolar ($): Representa el final de la cadena.

Alternativas en corchetes:
- Podemos usar corchete para especificar conjuntos de caracteres deseado. Ejem: [a-h] coincidirá con cualquier letra de la a a la h.

Operador de complemento:
- El simbolo de intercalación dentro de los corchetes excluye caracteres. Ejem: [^123] conciderá cualquier carácter excepto 1, 2 o 3.

Símbolo de interrogación y repeticiones:
- El símbolo de interrogación indica 0 o 1 repeticicón de un carácter.
- El símbolo de más indica una o más repeticiones del carácter.
- Ejem: a? concide con 'a' o nada; b+ coincide con 'b' una o más veces.

Rangos y Atajos:
- Dentro de corchetes, podemos usar guiones para representar rangos.
- Ejemplo: [0-9] coincide con cualquier dígito.

Patrones comunes:
- \d: Representa cualquier dígito decimal.
- \D: Representa cualquier cosa que no sea un dígito decimal.
- \s: Significa caracteres de espacio en blanco (espacio, tabulador, etc).
- \S: Representa cualquier cosa que no sea un carácter de espacio en blanco.
- \w: Es un carácter de palabra (letras, números, guión bajo).
- \W: Es el opuesto de \w y representa todo excepto caracteres de palabra.

Agrupación alternativa:
- Los paréntesis () agrupan patrones. Ejem: (com|edu) busca 'com' o 'edu'.
- La barra vertical | significa 'o'. Así que (a|b) busca 'a' o 'b'.

Manejo de Espacios:
- Puedes usar [A-Za-z0-9] para aceptar letras, números y espacios.
- O, puedes usar [\w\s] para incluir caracteres de palabra y espacios.

Sensibilidad a Mayúsculas:
- \w maneja tanto minúsculas como mayúsculas.
- Si es necesario, puedes forzar la entrada de minúsculas con lower() o convertir la expresión a minúscula.

Banderas de re.search:
- re.IGNORECASE: Permite que la búsqueda ignore las diferencias entre mayúsculas y minúsculas.
- re.MULTILINE: Configura la función para reconocer patrones en varias líneas de texto.

Explorando las funciones:
- re.match: Inicia la coincidencia desde el principio de la cadena sin la necesidad de '^'
- re.fullmatch: Coincide con el inicio y el final de la cadena, sin '^' o '$'

> Utiles cuando se recopilan datos de formularios, como Google Forms, ya que los usuarios pueden introducir información con formatos diversos.