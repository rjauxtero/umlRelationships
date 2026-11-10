#Association(Knows-a)
class Driver:
    def __init__(self,name: str):
        self.name = name

class Car:
    def __init__(self, model: str):
        self.model = model
        self.driver = None

    def assign_driver(self, driver: Driver):
        self.driver = driver

d = Driver("Rebecca")
c = Car("Sedan")
c.assign_driver(d)
print(f"{c.driver.name} is driving the {c.model}")