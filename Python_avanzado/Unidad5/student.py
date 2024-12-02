#Programa usando programación orientada a objetos

class Student:
    #... marcador de paso
    
    #house = None, convierte el atributo en opcional
    def __init__(self, name, last, house, patronus): #Es como el constructor
        self.last = last
        self.name = name 
        self.house = house 
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    #getter
    @property
    def house(self):
        return self._house
    
    #setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
        
    
     #Creación metodo propio para lanzar un hechizo mágico
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Rusell terrier":
                return "🐕‍🦺"
            case _:
                return "🪄"
         

#Abstracción
def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")


def get_student():
    name = input("Name: ")
    last = input("Last: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, last, house, patronus) #instancia del constructor


'''def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student'''

'''def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #tuple'''

'''def get_student():
    student = {} #incializar diccionario
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student'''
    
def main():
    '''name = get_name()
    house = get_house()'''

    #name, house = get_student()
    student = get_student()
    print(student)
    
    print("Expecto Patronum!")
    print(student.charm())
    
    #Método de clase
    '''student = Student.get()'''
    
    '''if student["name"] == "Padma":
        student["house"] = "Ravenclaw"'''
    #print(f"{student[0]} from {student[1]}")
    #print(f"{student['name']} from {student['house']}")
    #print(f"{student.name} from {student.house}")

    #las tuples no soportan la asignación de elementos0a
''' if student[0] == "Padma":
    student[1] == "Ravenclaw"'''
        

if __name__ == "__main__":
    main()
    