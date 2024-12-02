# Introducción a la programación avanzada

### UNIDAD 5

### Programación orientada a objetos (POO)

tuple: es una colección de valores, similar a una lista, pero con una característica fundamental, es inmutable. Esto significa que, una vez creada, no puedes cambiar sus elementos.

> Se recomienda su uso cuando necesitas almacenar datos que no deberian poder editarse.

> [!IMPORTANT] 
> Las tuplas no soporta la asignación de elementos

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

__str__ (The string Method): Este método especial se activa automáticamente cada vez que intentamos imprimir un objeto como una cadena, ofreciéndonos la oportunidad de definir cómo queremos que se vea esa representación.

## Definir una propia función __str__:
- Definir el método __str_ dentro de la clase, siguiendo el patrón def __str__(self):.
- Utilizar la referencia al objeto (self) para acceder a sus atributos y construir la cadena de representación que se desea.
- Retornar la cadena que se quiere imprimir cuando el objeto sea llamado con la función print.

## Diferencia entre __str__ y __repr__:
- __str__: Pensado para los usuarios fianles del programa, proporciona una representación legible del objeto.
- __repr__: Pensado para los desarrolladores, ofrece una representación detallada del objeto que incluye información sobre su tipo y estado interno.

Ejemplo de la creación de un método propio:
def charm(self):
Método que permité a un estudiante lanzar un hechizo mágico.

Propiedades (Getter y Setter): son herramientas que nos permiten controlar el acceso y la modificación de los atributos de una clase, lo qu enos brinda más control sobre cómo interactúan nuestros objetos y cómo se manejan los datos.

Propiedades:
- Nos permiten definir métodos especiales para acceder y modificar atributps de una clase de una manera más controlada y segura.
- Podemos encapsular la lógica para obtener y establecer valores de atributos, lo que nos permite realizar validaciones o realizar acciones adicionales cuandose accede o modifica un atributo.

Getter y Setter:
- Los getters son métodos que nos permiten obtener el valor de un atributo de una clase.
- Los setter son métodos que nos permiten establecer el valor de un atributo de una clase.
- Estos métodos nos ayudan a obtener la coherencia y la intergridad de nuestros datos al imponer reglas y validaciones sobre cómo se pueden acceder y modificar los atributos.

Implementación de Getter y Setters:
- Utilizaos la sintaxis @property para definir getter y setter.
- Los getter nos permiten acceder a los atributos de manera controlada, mientras que los setter nos permiten modificarlos de manera segura, aplicando lógica adicional si es necesario.

> se coloca _ al nombre de una setter, o getter para evitar conflictos en el caso de tener variables con el mismo nombre.

# getter
    @property
    def house(self):
        return self._house

Los tipos de datos como int, str, list y dict en realidad son clases en Python.
Cada vez que usamos estos tipos de datos, estamos creando objetos de esas clases.
> class int(x, base=10)
> class str(object='')
> class list([iterable])
docs.python.org/3/library/functions.html#int

Las clases viene con métodos, que son funcioens incorporadas que puedes ser llamadas sobre los objetos. Por ejemplo, lower() para convertir cadena a minúsculas y append() para agregar elementos a listas.
 > str.lower()
 > str.strip([chars])
 > list.append(x)
docs.python.org/3/library/stdypes.html#str
docs.python.org/3/library/stdypes.html#list
docs.python.org/3/library/stdypes.html#dict

 La función type() nos permite concer el tipo de un objeto en Python. Esto nos ayuda a entender mejor cómo Python maneja los datos y cómo podemos interactuar con ellos de manera efectiva.
 > print(type(50))

Métodos de clase: Son funciones asociadas a la clase en su conjunto, permitiéndonos operar a nivel de clase en lugar de instacias específicas. Se definen con el decorador @classmethod y acceden a la clase mediante el parámetro cls.

Variables de clase: Estas son compartidas por todas las instancias de la clase y se definen fuera de cualquier método. Son una manera eficiente de almacenar información a nivel de clase.