class Car:
    def __init__(self,userbrand,usermodel):
        self.brand=userbrand
        self.model=usermodel

    

my_car=Car("Toyota","Corola")
print(my_car.brand,my_car.model)


my_new_car=Car("Tata","Safari")
print(my_new_car.model)