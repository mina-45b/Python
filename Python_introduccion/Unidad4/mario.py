#DEPURACIÓN
#Programa que funciona como una piramide en mario bros

#Función principal
def main():
    #pide al usuario la altura de la piramide
    height = int(input("Height: "))
    #llama la función piramide y le pasa la altura
    pyramid(height)

#La función piramide espera el numero de la altura
def pyramid(n):
    #Imprime un número de hash
    for i in range(n):
        #Impresión de depuración
        #print(i, end=" ")
        print("#" * (i + 1))
      
        
#if __name__ == "__main___":

main()