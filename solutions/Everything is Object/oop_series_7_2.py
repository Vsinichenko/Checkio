#!/usr/bin/env checkio --domain=py run oop-series-7-2

# 7.1. Add thefuel_usedattribute inside__init__method ofCarclass without changing its arguments and assign it a value of0liters.
# 
# 7.2. Add thefuel_consumptionattribute inside__init__method ofCarclass, passing it as a method argument with default value of7(liters/100 km).
# 
# 7.3. Add adrivemethod to theCarclass that takes thedistanceargument of typeint(km). If an instance of class had started - incrementfuel_usedwith the proper value (that is based on fuel_consumption variable and distance parameter values) and display the message"Currently driven {distance} km, total fuel used - {fuel_used} l". If the instance had not started, display"Start the car before driving!"..
# 
# 7.4. Rewrite the method for theElectricCarclass, add and do not incrementfuel_used(since electric car doesn't used fuel), change the successful message to"Currently driven {distance} km on electric motor", keep the unsuccessful message unchanged.
# 
# 
# END_DESC

# show me some OOP magic here

# show me some OOP magic here
class Car():
    def __init__(self, brand="", model="", fuel_consumption=7):
        self.brand = brand
        self.model=model
        self.fuel_consumption=fuel_consumption
        self.fuel_used=0
    
    wheels = "four"
    doors=4
    working_engine=False
    unsuccessfull_drive_msg="Start the car before driving!"
    
    def start_engine(self):
        self.working_engine=True
        print("Engine has started")
        
    def stop_engine(self):
        self.working_engine=False
        print("Engine has stopped")
        
    def drive(self, distance: int):
        if self.working_engine:
            fuel_used_now = self.fuel_consumption*distance/100
            self.fuel_used+=fuel_used_now
            print(f"Currently driven {distance} km, total fuel used - {self.fuel_used} l")
        else:
            print(self.unsuccessfull_drive_msg)
        
    
    
# show me some OOP magic here
class ElectricCar(Car):
    def __init__(self, battery_capacity:int, brand="", model=""):
        super().__init__(brand, model)
        self.battery_capacity=battery_capacity
       
    
    def start_engine(self):
        self.working_engine=True
        print("Electric motor has started")
        
    def stop_engine(self):
        self.working_engine=False
        print("Electric motor has stopped")
        
        
    def drive(self, distance: int):
        if self.working_engine:
            print(f"Currently driven {distance} km on electric motor")
        else:
            print(self.unsuccessfull_drive_msg)
        

        
my_car = Car()
some_car1 = Car("Ford", "Mustang")
some_car2 = Car(model="Camaro")
some_car1.start_engine()
some_car2.start_engine()

some_car1.drive(10)


       
my_electric_car= ElectricCar(100, "Tesla", "Model 3")
my_electric_car.start_engine()


my_electric_car2=ElectricCar(60, "Toyota", "Prius")
my_electric_car2.start_engine()
my_electric_car2.stop_engine()
my_electric_car2.drive(1)


my_electric_car.drive(1)