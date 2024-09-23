#Simple calculadora

#OPCION 1
'''x = 1
y = 2

z = x + y

print(z)'''

#Calculadora interactiva

#OPCION 2 ENTEROS
'''x = int(input("what's x? "))
y = int(input("what's y? "))

#El resultado será una cadena concetenada, ya que input recibe texto
#z = x + y

#Convertir datos
#z = int(x) + int(y)
#print(z)

print(x + y)'''


#OPCION 3 FLOTANTES
'''x = float(input("what's x? "))
y = float(input("what's y? "))

#Redondear al entero más cercano
z = round(x + y)

#Formatear z
print(f"{z:,}")'''

#OPCION 4 DIVISIÓN
x = float(input("what's x? "))
y = float(input("what's y? "))

#Formatear - v1
#z = round(x / y, 2)
z = x / y

#Formatear - v2
print(f"{z:.2f}")

