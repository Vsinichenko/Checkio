#!/usr/bin/env checkio --domain=py run oop-series-6

# 6.1. Rewritestart_engineandstop_enginemethods of theElectricCarclass to display another messages"Electric motor has started"and"Electric motor has stopped"respectively and change attributes the same way.
# 
# 6.2. Call thestart_enginemethod for themy_electric_carinstance.
# 
# 6.3. Createmy_electric_car2(values60, "Toyota", "Prius"), start and stop its engine.
# 
# 
# END_DESC

#!/home/valentyna-sinichenko/miniconda3/envs/checkio/bin/checkio --domain=py run oop-series-6










# Taken from mission OOP 5: Parent - Child

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
       
    
    def start_engine(self):
        self.working_engine=True
        print("Electric motor has started")
        
    def stop_engine(self):
        self.working_engine=False
        print("Electric motor has stopped")
        
        
my_electric_car= ElectricCar(100, "Tesla", "Model 3")
my_electric_car.start_engine()


my_electric_car2=ElectricCar(60, "Toyota", "Prius")
my_electric_car2.start_engine()
my_electric_car2.stop_engine()
# show me some OOP magic here