class Car:
    def __init__(self,userbrand,usermodel):
        self.__brand=userbrand
        self.model=usermodel

    def get_brand(self):
        return self.__brand +"!"

    def full_name(self):
        return f"{self.__brand} {self.model}"

class ELectric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size


my_tesla=ELectric_Car("Tesla","Model_s","50kwh")
# print(my_tesla.__brand, my_tesla.model, my_tesla.battery_size)
print(my_tesla.full_name())
print(my_tesla.get_brand())

# my_car=Car("Toyota","Corola")
# print(my_car.brand,my_car.model)
# print(my_car.full_name())


# my_new_car=Car("Tata","Safari")
# print(my_new_car.model)