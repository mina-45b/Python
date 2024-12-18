#Programa que imprime un numero de ovejas simulando la practica que se hace antes de dormir
def main():
    n = int(input("What's n? "))
    
    for s in sheep(n):
        print(s)
    
    '''for i in range(n):
        print(sheep(i))'''

''' for i in range(n):
        print("🐑" * i)'''

def sheep(n):
    
    for i in range(n):
        yield "🐑" * i
    
    #return "🐑" * n
    
    #flock = []
    '''for i in range(n):
        flock.append("🐑" * i)
    return flock'''
    
    
        
if __name__ == "__main__":
    main()