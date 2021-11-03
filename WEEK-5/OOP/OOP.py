class Person:
    @staticmethod
    def static_method():
        return 'I am availe from the class'
    def __init__(self, firstname, lastname, age, country):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.skills = []
    def get_perrson_info(self):
        return f'He is {self.firstname} {self.lastname}. He is from {self.country}. He is {self.age} years old.'
    def add_skill(self, skill):
        self.skills.append(skill)
    def get_skills(self):
        result = ', '.join(self.skills) if len( self.skills) > 0 else 'No skills'
        return result

p = Person('John','Doe', 25, 'UK')
print(p)
print(p.get_perrson_info())

p.add_skill('HTML')
p.add_skill('CSS')
p.add_skill('JS')
p.add_skill('React')
p.add_skill('Python')
print(p.get_skills())

# Inheritance // creating a child / creating is gone be so easy using Python
# 

class Student(Person):
    def __init__(self, firstname, lastname, age, country, gender):
        self.gender = gender
        self.hobbies = []
        self.points = 0
        super().__init__(firstname, lastname, age, country)

    def get_perrson_info(self):
        pronoun =  'He' if self.gender == 'Male' else 'She'
        result = ', '.join(self.skills) if len( self.skills) > 0 else ''
        statement = result and f'{pronoun} has the following skills:{result}.'
        return f'{pronoun} is {self.firstname} {self.lastname}. {pronoun} is from {self.country}. {pronoun} is {self.age} years old. {statement} '
    def add_hoby(self, hobby):
        self.hobbies.append(hobby)
    def get_hobbies(self):
        return self.hobbies
    def add_point(self, point = 5):
        self.points = self.points + point
    def get_points(self):
        return self.points
    

s = Student('Elina', 'Sami', 21, 'Finland', 'Female')
print(s.firstname)

s.add_skill('Python')
s.add_skill('Git and GitHub')
s.add_skill('React')
s.add_skill('Data Analysis')
print(s.get_perrson_info())

print(s.get_skills())
s.add_point()
print(s.get_skills())
s.add_point(95)
print(s.get_points())

print(Person.static_method())


class Animal:
    def _init__(self, name, age, legs):
        self.name = name
        self.age = age
        self.legs = legs
    def methods_class(self):
        pass

dog = Animal('Fluffy',8, 4)
cat = Animal('Murri',4, 4)
