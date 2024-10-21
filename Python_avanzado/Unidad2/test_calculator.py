#Importamos calculadora
from calculator import squared as sq

#Definimos la función principal
def main():
    test_square()

#Definimos la función de prueba
def test_square():
    try:
        #El cuadrado debe ser igual a... muestra la línea de código donde fallo
        assert sq(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    
    try:
        assert sq(3) == 9
    except AssertionError:
        print("3 squared was not 9")
        
    try:
        assert sq(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
        
    try:
        assert sq(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
        
    try:
        assert sq(0) == 0
    except AssertionError:
        print("0 squared was not 0")
        
        #opción 1
'''  if sq(2) != 4:
        print("2 squared was not 4")
    if sq(3) != 9:
        print("3 squared was not 9")'''

#función condicional
if __name__ == "__main__":
    main()