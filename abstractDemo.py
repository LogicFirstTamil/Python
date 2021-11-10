from abc import ABC, abstractmethod
## You cannot create object for abstract class
## Classes inheriting abstract class must override all abstract methods

class Vehicle(ABC):   #abstract class
    @abstractmethod #decorator
    def start(self):
        pass

class Bike(Vehicle): #concrete class
    color = None
    def start(self):
        print("You are riding a bike....")

class Car(Vehicle):
    color = None
    def start(self):
        print("You are riding a car...")
