#Inheritance(Is-a)
class Animal:
    def __init__(self,name):
        self.name = name

#Mouse inherits from Animal
class Mouse(Animal):
    def speak(self):
        return f"{self.name} says Squeak!"

myMouse = Mouse("Silvie")
print (f"{myMouse.speak()}")
