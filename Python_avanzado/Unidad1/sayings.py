#programa de ejemplo para crear una libraría personalizada

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello,{name}")
    
def goodbye(name):
    print(f"goodbye,{name}")

#Al crear una librería para uso común no se debe utilizar main() para evitar una llamada innecesaria o inadecuada 
#main()

if __name__ == "__main__":
    main()