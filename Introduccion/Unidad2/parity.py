#Busca el número par

def main():
    x = int(input("What's x?"))
    
    if is_even(x):
        print("Even")
    else:
        print("Odd")
    
def is_even(n):
    #OPCION 1
    '''if n % 2 == 0:
        return True
    else:
        return False'''
    
    #OPCION 2
    '''return True if n % 2 == 0 else False'''

    #OPCION 3
    return n % 2 == 0

main()

