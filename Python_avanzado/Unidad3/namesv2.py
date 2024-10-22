#Programa que lee un archivo con open

names = []

with open("Python_avanzado/Unidad3/names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names, reverse=True):
    print(f"hello, {name}")
    

'''with open("Python_avanzado/Unidad3/names.txt", "r") as file:
    #versión 2
    for line in file:
        print("hello,", line.rstrip())'''
        
'''    
#leer todas las lineas del archivo a la vez
    lines = file.readlines()
    
for line in lines:
    print("hello,", line.rstrip())'''