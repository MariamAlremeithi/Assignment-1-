class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

        car1 = Car("Camry", 2021)
        car2 = Car("porche", 2023)
        print(car1.model)
