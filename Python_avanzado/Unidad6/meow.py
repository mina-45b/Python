#Programa para ejemplificar type hints y mypy

#Determina el tipo que recibe la variable
'''def meow(n: int):
    for _ in range(n):
        print("meow")
        
number:int = int(input("Number: "))
meow(number)'''

def meow(n:int) -> str:
    '''
    Meow n veces
    :param n: Numero de veces de meow
    :type n: int
    :raise TypeError: Si n no es un int
    :return: un string con n meows, uno por línea
    :rtype: str
    '''
    return "meow\n"*n

number:int = int(input("Number: "))
meow:str = meow(number)
print(meow, end="")