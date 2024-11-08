#programa que valida una dirección de correo electrónico
import re

#.strip() elimina espacios a la izquierda y derecha
email = input("What's your mail? ").strip()

#opción 1
'''if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")'''
    
#opcion 2
'''username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")'''
    
#r cadena sin formato
if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
