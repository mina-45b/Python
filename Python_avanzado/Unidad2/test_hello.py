#Ejemplo de una prueba unitaria
from hello import hello

#Dividir por categoría las pruebas
def test_default():
    assert hello() == "hello, world"
    
def test_argument():
    for name in ["Hermanione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
        
    #assert hello("David") == "hello, David"