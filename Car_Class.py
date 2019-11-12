# Alex Bello
# 11/11/2019
# Defines the Class Car


class Car():
    def __init__(self, make, model, color, year, mileage, price):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
        self.price = price

    def description(self):
        print(f"""The cars make is {self.make} the model is {self.model} it's a {self.color} {self.year} {self.model}. 
It has {self.mileage} miles on it and I only got it for {self.price} dollars!""")

    def change_color(self,new_color):
        self.color = new_color

    def odometer_update(self,more_miles):
        self.mileage += more_miles
