#Excepciones

'''try:
    #Error de valor - ValueError: invalid literal for int()
    x = int(input("What's x? "))
    print(f"x is {x}")
    
except ValueError:
    print("x is not an interger")'''
    
    
'''try:
    #Error de valor - ValueError: invalid literal for int()
    x = int(input("What's x? "))
    
except ValueError:
    print("x is not an interger")
    
#Error de nombre - NameError: name 'x' is not defined
print(f"x is {x}")'''

#OPCION 1
'''while True:
    try:
        #Error de valor - ValueError: invalid literal for int()
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an interger")
    else:
        break

#Error de nombre - NameError: name 'x' is not defined
print(f"x is {x}")'''

#OPCION 2
'''while True:
    try:
        #Error de valor - ValueError: invalid literal for int()
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an interger")
      

#Error de nombre - NameError: name 'x' is not defined
print(f"x is {x}")'''

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            #x = int(input("What's x? "))
            return int(input(prompt))
        except ValueError:
            print("x is not an interger")
            #pass
        '''else:
            #break
            return x #saca del bucle y devuelve el valor'''
        
main()