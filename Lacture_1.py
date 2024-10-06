#class 

import math

class cylinder():
    def __init__(self,r,h):
        self.r = r
        self.h = h

    def calculate(self):
        v = math.pi*self.r**2*self.h
        return v
    
    def area(self):
        a = math.pi*self.r**2
        return a 


first_cylinder = cylinder(5,10)
secound_cyliner = cylinder(7,13)

print(first_cylinder.calculate())

print(secound_cyliner.calculate())

print(first_cylinder.area())

        
    
