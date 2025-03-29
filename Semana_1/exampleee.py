class Person:
    @staticmethod
    def static_method():
        print("n")
    @classmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def walk(self):
        print(f'{self.name} is walking') 
        

class Downperson (Person):
    def __init__(self, name, age, syndrome):
        self.name = name
        self.age = age
        self.syndrome = syndrome

Downperson.static_method()

person1 = Person("Esteban", 12)
print(person1.name.encode())

    
