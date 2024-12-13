#Programa para ejemplificar el uso de unpacking de Python

#Por convecion se usa "_" para nombrar variables que no se utilizan
'''first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")'''

def total(gelleons, sickles, knuts):
    return(gelleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
coins2 = {"galleons": 100, "sickles": 50, "knuts": 25}

'''print(total(galleons=100, sickles=50, knuts=25), "Knuts")'''

#Usamos "*" delante de la lista para desempaquetar
print(total(*coins), "Knuts")

#USamos "**" delante del diccionario para desempaquetar
print(total(**coins2), "Knuts")
