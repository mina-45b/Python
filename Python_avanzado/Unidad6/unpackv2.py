#Versión mejorada del programa unpack

def f(*args, **kwargs):
    print("Named:", kwargs)
    
f(galleons=100, sickles=50, knuts=25)