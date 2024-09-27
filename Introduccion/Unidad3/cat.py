#Programa que maulla como cato

#OPCION 1
'''print("meow")
print("meow")
print("meow")'''

#OPCION 2
'''i = 3
while i != 0:
    print("meow")
    i = i - 1'''

#OPCION 3 while
'''i = 0
while i < 3:
    print("meow")
    i += 1'''

#OPCION 4 for
'''for i in range(3):
    print("meow")'''
    
#OPCION 5
'''for _ in range(3):
    print("meow")'''

#OPCION 6
'''print("meow\n" * 3, end="")'''

#OPCION 7
'''while True:
    n = int(input("What's n? "))
    if n > 0:
        break
    
for _ in range(n):
    print("meow")'''
    
#OPCION 8
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
    
def meow(n):
    for _ in range(n):
        print("meow")
        
main()