class Car:
    def __init__(self, brand_name,brand_speed):
        self.__brand_name=brand_name
        self.brand_speed=brand_speed

    def get_brand(self):
        return self.__brand_name

    def full_name(self):
        return f"The speed of the {self.brand_name} is {self.brand_speed}."

    def fuel_type(self):
        return "Petrol or Diseal."

class Electric_Car(Car):
    def __init__(self, brand_name, brand_speed, battery_size):
        super().__init__(brand_name,brand_speed)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"

tesla=Electric_Car("Tesla", "120km/h", "85kwh")
print(tesla.battery_size)
print(tesla.fuel_type())

my_car=Car("Toyota","100km/h")
print(my_car.brand_speed)
print(my_car.get_brand())
print(my_car.fuel_type())
# print(my_car.full_name())   

my_new_car=Car("Tata","150km/h")
print(my_new_car.get_brand())
print(my_new_car.brand_speed)
