#Programa que tiene una lista de estudiantes

#Lista de alumnos - diccionarios
students = {
    "Hermione": "Gryffindor",
    "Harry":  "Gryffindor",
    "Ron":  "Gryffindor",
    "Draco": "Slytherin",
}

#Uso de indices para imprimir

#OPCION 1
'''print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])'''

#OPCION 2
for student in students:
    print(student, students[student], sep=", ")