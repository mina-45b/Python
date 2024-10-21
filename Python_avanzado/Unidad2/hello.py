#Función principal
def main():

    name = input("What's your name? ")
    print(hello(name))
    

def hello(to="world"):
    #print("hello,",to)
    return f"hello, {to}"
    
#Llamar a mi función principal
if __name__ == "__main__":
    main()