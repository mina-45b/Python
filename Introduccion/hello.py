
#Imprimir texto por pantalla
#print("hello, world")

#Pedir al usuario su nombre

#OPCION 1
'''print('what\'s your "name?"')
#entrada de argumentos por el usuario
name = input()
print("hello,", end=' ')
print(name)'''

#OPCION 2 
#Preguntar el nombre del usuario
name = input("what's your \"name?\" ")

#Remover espacios en blanco
name = name.strip()

#Poner en mayúscula la primera letra de la entrada 
#name = name.capitalize()

#Poner en mayúscula la primera letra de la entrada basado en el titulo
#name = name.title()

#OPCION 4
name = name.strip().title()

#Dividir el nombre en  nombre y apellido
first, last = name.split(" ")

#OPCION 5
#name = input("What's your name? ").strip().title()

#Decir hola al usuario
print("hello, "+first)

#OPCION 3
print(f"hello, {name}")



