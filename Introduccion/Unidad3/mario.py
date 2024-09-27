#Programa que replica uel funcionamiento de algunos objetos en mario bros

#OPCION 1
'''print("#")
print("#")
print("#")'''

#OPCION 2
'''for _ in range(3):
    print("#")'''
    
#OPCION 3
def main():
    #Abstracción del problema
    print_column(3)
    print_row(4)
    print_square(3)
    
def print_column(height):
    #OPCION 1
    '''for _ in range(height):
        print("#")'''
        
    #OPCION 2
    print("#\n" * height, end="")
    
def print_row(width):
    print("?" * width)
    
def print_square(size):
    #Bucles anidados
    
    #OPCION 1
    '''#Para cada fila en el cuadrado
    for i in range(size):
        #Para cada ladrillo en la fila
        for j in range(size):
            #Imprimir ladrillo
            print("#", end="")
        #Salta a la siguiente línea
        print()'''
        
    #OPCION 2
    for i in range(size):
        print_row_square(size)
        
def print_row_square(width):
    print("#" * width)
    
main()