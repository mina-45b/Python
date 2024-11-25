#Programa usando programación orientada a objetos

class Student:
    #... marcador de paso
    
    #house = None, convierte el atributo en opcional
    def __init__(self, name, last, house): #Es como el constructor
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.last = last
        self.name = name 
        self.house = house 
        

def main():
    '''name = get_name()
    house = get_house()'''

    #name, house = get_student()
    student = get_student()
    '''if student["name"] == "Padma":
        student["house"] = "Ravenclaw"'''
    #print(f"{student[0]} from {student[1]}")
    #print(f"{student['name']} from {student['house']}")
    print(f"{student.name} from {student.house}")

    #las tuples no soportan la asignación de elementos0a
''' if student[0] == "Padma":
    student[1] == "Ravenclaw"'''
    

#Abstracción
def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

def get_student():
    name = input("Name: ")
    last = input("Last: ")
    house = input("House: ")
    return Student(name, last, house) #instancia del constructor


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

if __name__ == "__main__":
    main()
    