
students = [] #lista

with open("Python_avanzado/Unidad3/students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {} #diccionario
        student["name"] = name
        student["house"] = house
        students.append(student)
        
        #Opcion 1
        '''row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")'''
        
def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}")
        
#Opcion 1
'''for student in sorted(students, key=get_name, reverse=True):
        print(f"{student['name']} is in {student['house']}")'''
        
   
        
    