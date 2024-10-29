import csv

students = []

with open("Python_avanzado/Unidad3/studentsv2.csv") as file:
    #reader = csv.reader(file)
    reader = csv.DictReader(file)
    
    #for name, home in reader:
        #students.append({"name": name, "home": home})
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
    
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")