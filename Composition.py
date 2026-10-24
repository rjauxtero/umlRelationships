#Composition
class Classroom:
    def __init__(self,name: str):
        self.name = name

class School:
    def __init__(self):
        self.classrooms = [Classroom("Math Room"), Classroom("Science Room")]

myClassroom = School()
print ("School contains classrooms", [Classroom.name for Classroom in myClassroom.classrooms])