#Programa que tiene una lista de estudiantes

#Lista de alumnos - list
students = ["Hermione", "Harry", "Ron", "Draco"]

#Imprimir el contenido de una lista

#OPCION 1
'''print(students[0])
print(students[1])
print(students[2])'''

#OPCION 2
'''for student in students:
    print(student)'''

#OPCION 3
#longuitud de estudianes es el rango en el que se itera
'''for i in range(len(students)):
    print(students[i])
    '''
    
#OPCION 4
for i in range(len(students)):
    print(i + 1, students[i])
    
