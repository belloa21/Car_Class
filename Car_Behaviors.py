from Car_Class import Car

make = "Pontiac"

model = "Sunfire"

color = "Blue"

year = "2006"

mileage = 50000

price = "1,500"

#Car.description()


my_car = Car(make, model, color, year, mileage, price)
my_car.description()
my_car.change_color("Green")
my_car.odometer_update(1002)
my_car.description()
