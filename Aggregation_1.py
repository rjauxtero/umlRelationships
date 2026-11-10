#Aggregation(Weak Has-a)
class Professor:
    def __init__(self, name: str):
        self.name = name

class Course:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professors(self, prof:Professor):
        self.professors.append(prof)

prof1 = Professor("Mr. Dela Cruz")
course1 = Course("Mathematics")
course1.add_professors(prof1)
print(f"Course: {course1.name}, Professor: {course1.professors[0].name}")