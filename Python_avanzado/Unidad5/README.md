Introducción a la programación avanzada

UNIDAD 5

Programación orientada a objetos (POO)

tuple: es una colección de valores, similar a una lista, pero con una característica fundamental, es inmutable. Esto significa que, una vez creada, no puedes cambiar sus elementos.

>Se recomienda su uso cuando necesitas almacenar datos que no deberian poder editarse.

>[!IMPORTANT] 
>Las tuplas no soporta la asignación de elementos

Diccionarios (objetos dict): son colecciones de claves y valores.

La gran ventaja de los diccionarios radica en su semántica: en lugar de depender de índices numéricos, asociamos claves descriptivas con sus respectivos valores.

Clase: es como un plano o molde que te permite crear tus propios tipos de datos personalizados.

Documentación: docs.python.org/3/tutorial/classes.html

Los objetos se crean (instancian) utilizando el nombre de la clase seguido de paréntesis.

Ejm. student = Student()

Los objetos pueden tener atributos que los diferencien.

Ejm. student.name

Métodos de instancia: son funciones definidas dentro de una clase que operan en instancias específicas de esa clase. Son esenciales para inicializar y personalizar objetos, permitiéndonos definir su comportamiento y características únicas.

- Método __init__: Este método especial, conocido como el constructor de la clase, se utiliza para inicializar objetos. A través de este método, podemos asignar valores a als varibales de instancia del objeto.

Ejem. def __init__(name, house)

- Uso del parámetro self: El parámetro self hace referencia al objeto actual y nos permite acceder y manipular sus atributos dentro de los métodos de instancia.

Ejem. def __init__(self, name, house)

- Personalización de objetos: Mediante el método __init__, podemos personalizar los atributos de un objeto al crearlo, definiendo valores iniciales para sus variables de instancia.

Ejme. def __init__(self, name, house):
                self.name = name
                self.house = house

- Validación de datos: Podemos implementar lógica de validación dentro del método __init__ para garantizar que los objetos se creen con datos váidos y coherentes.

Ejem. def __init__(self, name, house):
            if not name:
                return None
            self.name = name
            self.house = house

- Excepciones personalizadas: Utilizando la plabra clave raise, podemos lanzar nuestras propias excepciones cuando ocurren situaciones excepcionales durante la inicialización de objetos.

Ejem.   if not name:
            raise ValueError("Missing name")