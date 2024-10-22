#Programa que recoge los nombres de los estudiantes
'''names = []

#se usa "_" en lugar de i, j, k... cuando no se utilizará la variable de la iteración
for _ in range(3):

    #name = input("What's your name? ")
    names.append(input("What's your name? "))

#sorted() devuelve una versión ordenada de la lista
for name in sorted(names):
    print(f"hello, {name}")'''
    
#OPCION USANDO OPEN
name = input("What's your name? ")

#sobre escribe en el archivo
#file = open("Python_avanzado/Unidad3/names.txt", "w")
#appen añade al archivo
'''file = open("Python_avanzado/Unidad3/names.txt", "a")
file.write(f"{name}\n")
file.close()'''

with open ("Python_avanzado/Unidad3/names.txt", "a") as file:
    file.write(f"{name}\n")