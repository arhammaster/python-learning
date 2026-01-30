class Car:

    def __init__ (self,model,make,color,year):
        self.model = model
        self.make = make
        self.type = color
        self.year = year

    def start (self):
        print(f"{self.model} has started")

    def stop (self):
        print(f"{self.model} has stopped")

    def horn (self):
        print(f"{self.model} has pressed the horn")

car = Car ("Mustang","Ford","Grey","2025")

car.start()
car.stop()
car.horn()
