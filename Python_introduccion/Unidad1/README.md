# Introducción a la programación con Python

## UNIDAD 1 

**Python** es un intérprete.

*Funciones:* acción que permite hacer algo en el programa. La mayoría
de los lenguajes tienen funciones predetermindas.

**Ejem.** -> Función: print -> print("hello, world")

*Argumentos:* entrada a una función que influye en su comportamiento.

**Ejem.** -> Argumento: hello, world -> print("hello, world")

*Bugs:* es un error en un programa.

*Variables:* almacenan valores, número, texto... es un contenedor dentro de un 
ordenador o programa.

*Comentarios:* notas en el código que no son interpretadas.

**Ejem.** 
- Una línea: # -> #Esta es mi nota
- Multilínea: ''' ... ''' o """ ... """

*Pseudocódigo:* es una forma de expresar una idea, ayuda a estructurar y planificar un programa.

Divide tareas grandes en pequeñas tareas que se pueden ejecutar con mayor facilidad.

**Ejem.** #paso 1 ... #paso 2 ...

> [!NOTE]
> **_input_** solo espera cadenas de texto.

*Espacios:* se agregan con fines estéticos para la comprensión de la lengua. 

**Ejem.** -> print("hello, ", name)

*Múltiples argumentos:* algunas funciones puden recibir varios argumentos.

**Ejem.** -> , -> print("hello,",name)
> La ',' nos sirve para separar los argumentos

*Concatenar:* permite unir cadenas de texto.

 **Ejem.** -> + -> "hello, " + name

> [!NOTE]
> Cadenas - _str_

*Paramétros:* entradas que pasas a una función. def(a,b)
*Argumentos:* cuando usas la función y pasas los datos. def("juan","lara")

### FUNCIÓN PRINT 

Si buscamos en la documentación [docs.python.org](https://docs.python.org/3/) encontraremos información de como funcionan las funcines predetermindas de Python.

En este ejemplo tenemos la función Print:
> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

### Paramétros con nombre:

- *objects -> signfica que puedo tomar cualquier número de objetos.
- sep=' ' -> otro paramétro que introduce por defecto un espacio en blanco.
- end='\n' -> significa que al terminar la función se crea un salto de línea.

*Caracteres de escape:* son caracteres que nos permiten usar caracteres definidos dentro del lenguaje sin  generar conflictos.

**Ejem.**
-> ' ' -> print('hello, "friend"')
->  \ -> print("hello, \"friend\"")

*Cadena de formato o f-String:* permiten formatear un cadena de forma especial.

**Ejem.** -> f  { }-> print(f"hello, {name}")

*Método:* es una función que se construye en un tipo de valor.

### MÉTODOS DE CADENAS 

- Remover espacios en blanco: **Ejem.** name = name.strip() - lstrip() / rstrip()
- Poner en mayúsculas la primera letra de la entrada del usuario: name = name.capitalize()
- Capitalizar (poner en mayúsculas la primera letra de la entrada) basado en el titulo: name = name.title()
- Dividir una cadena en varias cadenas más pequeñas: **Ejem.** name.split(" ")

> [!NOTE]
> entero - _int_

### OPERADORES
- Suma +: agrega dos números
- Resta -: sustrae el segundo número del primero.
- Múltiplicación *: multiplica dos números.
- División /: divide el primer número por el segundo.
- Módulo %: da el resto de una división.

*Modo interactivo:* es cuando se ejecuta el interprete sin la necesidad de crear un archivo.

*Conversión de tipos:* es la capacidad de cambiar un tipo de dato a otro.

> [!NOTE]
> flotante - _float_

*float:* decimal, valor de punto flotante.

*Redondear valor:* round, redondea al entero más cercano.
> round(number[, ndigits])

**Paramétros:**
- number: recibe un número, si no se selecciona digitos, redondea al entero más cercano.
- ndigits: especifica cuantos digitos debe tener.

*Formato númerico:* trata de presentar números de manera legible y visualmente atractiva.

> [!NOTE]
> Los decimales float, no representan datos con una presición exacta.

> [!NOTE]
> definir - _def_

*Ámbito(scope):* se refiere al alcance en el que una variable puede ser utilizada.
Una variable solo existe en el contexto en elque ha sido definida.

**Ejem.** -> def main():
                name = input("What's your name? ")
                hello(name)

> [!NOTE]
> valores de retorno - return

*Valores de retorno:* son la joya que una función entrega después de realizar ciertas acciones.
