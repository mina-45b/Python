#programa que valida una dirección de correo electrónico

#.strip() elimina espacios a la izquierda y derecha
email = input("What's your mail? ").strip()

#opción 1
'''if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")'''
    
#opcion 2
username, domain = email.split("@")

if username:
    print("Valid")
else:
    print("Invalid")