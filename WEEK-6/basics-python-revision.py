# Fundamental of Programmng
# Variables 

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'

# comment , a single line comment
# to make our code readable ourselves
# Data types
# Numbers(Int, Float, Complex), Booleans, Strings
# List

age = 250
height = 1.73
gravity = 9.81
pi = 3.14
mass = 75
complex_num = 1 + 2j
print(type(complex_num))

# Arithmetic Operation : +, -, *, /, %, //, **
radius = 10
area = pi * radius ** 2
print(area)

weight = mass * gravity
print(weight)

a = 9
b = 5

print(f'The su of {a} and {b} is {a + b}.')
print(f'The sum is ', a  + b)
print(f'The difference of {a} and b is {a - b}.')
print(f'The product of {a} and {b} is {a * b}.')
print(f'The division of {a} and {b} is {a / b}', )
print(f'The floor division of {a} and {b} is {a // b}.')
print(f'The remainder of {b} divided by {a} {b % a}')
print(f'{b} the power of {a} is {b ** a}.')

print('{1} + {0} = {2}'.format(a, b, a + b))
print('{}{}'.format('water', 'mellon'))

# Function: builtin function and custom function
# print('hello', 'world', 2021, 'whatsovever'), type()
# len(), input(), round() ..

# String 
# a single or double quoate

l = 'a'
print(len(l))
sentence = 'It could be as long as a sentence, paragraph or a page'
print(len(sentence))
print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print(sentence.swapcase())
print(sentence.startswith('It '))
print(sentence.endswith('page'))
print(sentence.replace(',', ''))
sentence = sentence.replace(',', '')
print(sentence.split())

langauge = 'Python'
print(langauge[0])
print(langauge[1])
print(langauge[-1])
print(list(langauge))

for l in langauge:
    print(l)

# Booleans: True or False

print(1 > 0)
print(1 < 0)

happy = False
if happy :
    print('Open vscode and write some Python script')
else:
    print('Try to be be happy first')
    
a = -10
if a > 0:
    print(f'{a} is positive number.')
elif a == 0:
    print(f'{a} is zero')
elif a < 0:
    print(f'{a} is negative number')
else:
    print('not a number')

print(list(range(3, 10, 3)))


evens = list(range(0, 101, 2))
print(evens)

odds = list(range(0, 101, 2))
print(odds)  

nums = [1, 2, 3, 4] # append, pop, extend, etc
nums.insert(2, 100)
nums.extend([4, 6, 7, 8, 9, 10])
print(nums)
# append, pop, extend, insert

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print(nums1 + nums2)
countries = ['Finland','Sweden','Norway']
cities = ['Helsinki','Stockholm','Oslo']
print(list(zip(countries, cities)))

for country, city in zip(countries, cities):
    print(country, city)
    
    
    
print(list(enumerate(countries)))

for i, country in enumerate(countries):
    print(f'{i + 1}. {country}')


# Tuples, set, Dictionary

nums_set = set([1, 2, 3, 4, 4, 2, 1, 3])
print(nums_set)

fin_to_eng = {
    'sana':'word',
    'talo':'house',
    'puhu':'speak'
}

print(fin_to_eng['sana'])
print(fin_to_eng['talo'])
print(fin_to_eng['puhu'])

from pprint import pprint
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
   'age': 250,
    'skills':['HTML','CSS','JS'],
    'is_married':True,
    'address':{
        'city':'Helsinki',
        'street_name':'Space Street',
        'zipcode':'0200'
    }
}

person['age'] = 150
person['nationality'] = 'Ethiopian'

keys = person.keys()
pprint(keys)
values = person.values()
pprint(values)
items = person.items()
print(items)
# for key, value in items:
#     print(value)

print(person.get('nationality'))