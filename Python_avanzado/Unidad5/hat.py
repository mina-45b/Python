#Programa que simula el sombrero seleccionador de Harry Potter

import random


class Hat:
    #se elimina el init, por que no se crearán muchos objetos de hat
    '''def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]'''
        
    #Variable d eclase
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
    #método de clase
    @classmethod
    def  sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
    
    
Hat.sort("Harry")