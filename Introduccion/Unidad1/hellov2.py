#Definir una función llamada hello

#Función principal
def main():
    #hello()
    name = input("What's your name? ")
    hello(name)


#Función llamada hello que recibe un paramétro llamado to y en caso que no se defina
#el paramétro se utilizará world
def hello(to="world"):
    print("hello,",to)
    
#Llamar a mi función principal
main()