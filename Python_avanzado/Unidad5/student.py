#Programa usando programación orientada a objetos

def main():
    '''name = get_name()
    house = get_house()'''

    #name, house = get_student()
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    #print(f"{student[0]} from {student[1]}")
    print(f"{student['name']} from {student['house']}")

    #las tuples no soportan la asignación de elementos
''' if student[0] == "Padma":
    student[1] == "Ravenclaw"'''
    

#Abstracción
def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

'''def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #tuple'''

def get_student():
    student = {} #incializar diccionario
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()
    