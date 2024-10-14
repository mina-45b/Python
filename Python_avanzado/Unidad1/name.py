import sys

#Opcion 1
'''try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")'''
    
#Opcion 2
'''if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])'''

#Opcion 3
'''if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")


print("hello, my name is", sys.argv[1])'''

#Opcion 4
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg)