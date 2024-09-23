#Defino la función principal
def main():
    x = int(input("What's x? "))
    print("x squared is", squared(x))
    
def squared(n):
    #Retorna el cuadrado de un valor
    #return n * n
    #Elevar a la potencia de la derecha v1
    #return n ** 2
    #Elevara la potencia v2
    return pow(n, 2)
    
main()