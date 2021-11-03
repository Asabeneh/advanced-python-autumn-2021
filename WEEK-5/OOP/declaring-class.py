# Class

class Car:
    def __init__(self, model, brand, greabox, color) :
        self.model = model
        self.brand = brand
        self.gearbox = greabox
        self.color = color

toyota = Car(2021,'Toyota Corolla', 'Automatic','Blue black')
print(toyota.model)


class Dog:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

d1 = Dog('Fluffy',8, 'Greece')
print(d1.name)
print(d1.age)
print(d1.country)

d2 = Dog('Husky', 10, 'Finland')
print(d2.name)
print(d2.age)
print(d2.country)

class NameOfClass:
    def __init__(self, name, gender, country):
        self.name = name
        self.gender = gender
        self.country = country

ob = NameOfClass('John', 'Male','UK')