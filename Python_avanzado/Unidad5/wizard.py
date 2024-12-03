#Programa utilizado para aprender sobre la herencia de clases

#Super clase
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

#Clases que heredan
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
        

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
Wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Darj Arts")
        
