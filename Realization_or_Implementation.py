#Realization/Implementation(Implements)
from abc import ABC, abstractmethod

class Renderable(ABC):
    @abstractmethod
    def render(self):
        pass

class Button(Renderable):
    def render(self):
        return "Rendering a graphical button component!"

btt = Button()
print(btt.render())