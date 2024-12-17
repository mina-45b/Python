students = ["Hermione", "Harry", "Ron"]

'''gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})'''
    
#gryffindors = [{"name": student, "house": "Gryfifindor"} for student in students]
 
gryffindors = {student: "Gryffindor" for student in students}
    
print(gryffindors)