#!/usr/bin/env checkio --domain=py run oop-series-5

# 5.1. Create anElectricCarclass that inherits properties from theCarclass.
# 
# 5.2. Modify the__init__method of theElectricCarclass so that it usessuper()to call the__init__method of theCarclass.
# 
# 5.3. Add a new attributebattery_capacityof typeintto theElectricCarclass__init__method. This attribute must be passing as argument. Put this argument beforebrandandmodel, because arguments without default values must go before ones that have.
# 
# 5.4. Create amy_electric_carinstance of theElectricCarclass, passingbattery_capacity, brand, modelwith values100, "Tesla", "Model 3"respectively.
# 
# 
# END_DESC

# Taken from mission OOP 4: Adding Methods

# Taken from mission OOP 3: Initializing
# Taken from mission OOP 2: Class Attributes
# Taken from mission OOP 1: First Look at Class and Object
# show me some OOP magic here
class Car():
    def __init__(self, brand="", model=""):
        self.brand = brand
        self.model=model
    
    wheels = "four"
    doors=4
    working_engine=False
    
    def start_engine(self):
        self.working_engine=True
        print("Engine has started")
        
    def stop_engine(self):
        self.working_engine=False
        print("Engine has stopped")
    
my_car = Car()
some_car1 = Car("Ford", "Mustang")
some_car2 = Car(model="Camaro")
some_car1.start_engine()
some_car2.start_engine()


# show me some OOP magic here
class ElectricCar(Car):
    def __init__(self, battery_capacity:int, brand="", model=""):
        super().__init__(brand, model)
        self.battery_capacity=battery_capacity
        
        
my_electric_car= ElectricCar(100, "Tesla", "Model 3")