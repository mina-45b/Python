#Programa para ejemplificar el uso de la función enumerate()

students = ["Herminoe", "Harry", "Ron"]

'''for i in range(len(students)):
    print(i +1, students[i])'''
    
    
for i, student in enumerate(students):
    print(i +1, student)