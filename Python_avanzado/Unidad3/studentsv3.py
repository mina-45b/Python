import csv

name = input("What's your name? ")
home = input("Where's your home? ")

#"a" modo append para añadir más datos
with open("Python_avanzado/Unidad3/studentsv3.csv", "a") as file:
    #writer = csv.writer(file)
    #writer.writerow([name, home])
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home":home})
    
    
    