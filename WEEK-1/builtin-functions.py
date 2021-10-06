# What is a function? 
# Function is a block of code that perform a certain task

import random
print(1, 2, 3)
print('Hi','Hello','whatever you in your mind')

'''
 print(), type(), round(), int(), float(), str(), input(),
 len(), sum(), min(), max(), list(), tuple(), dict(), eval(), abs(), bool(), enumerate(), map(), filter(), id(), sort(), sorted(), set(), zip
'''
print('Print allows to print something out')

# Type allow us to know the data type of a data
# Data types: Number(int, float, complex), string, bolean, list, dictionary, tuple, set
# 
""" print(type(10))
print(type(3.14))
print(type(1 + 2j))

print(type('2'))
print(type('Everyone loves Python'))
# Any data under single/double quote is a string

print(type(int('2')))

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
full_name = first_name + ' ' + last_name
print(full_name) """

'''
My name is Asabeneh Yetayeh. I am 250 years old. I live in Helsinki, Finland. 
'''

""" 
print('My name is ' + full_name + '. ' + 'I am ' + str(age) + ' years old. ' + ' I live in ' + city + ', ' + country + '.')

print(f'My name is {full_name}. I am {age} years old. I live in {city}, {country}.')
print(round(9.81, 1))
print(round(3.14, 1))
print(round(1.414))
print(round(2.51))
print(round(3.14141414141, 1))
print(round(4.56, 1))

print(float(2))
print(float('9.81'))
print(int(float('9.81')))
 """
# area of a circle area = pi * r * r

# radius = float(input('Enter a radius: '))

# area = 3.14 * radius * radius

# print(f'The area of the circle with {radius} m radius is {area} square meter.')

""" print(len(first_name))
print(len(last_name))
print(len([1, 2, 3, 4, 5, 'something', True, (1, 2, 3), {2, 3, 4}, {'lang':'Python'}]))
lst = [1, 2, 3, 4, 5, 'something', True, (1, 2, 3), {2, 3, 4}, {
    'lang': 'Python'}]

for item in lst:
    print(item, type(item)) """

""" print(min(1, 2, 3, 4))
print(max(1, 2, 3, 4))
print(max([1, 2, 3, 4]))
print(sum([1, 2, 3, 4]))
print(list({1, 2, 3, 4, 5}))
print(list((1, 2, 3, 4, 5)))
print(list({'name':'Asab','age':250}))

empty_list = list()
print(empty_list)
print(list('Python'))
print(abs(-5))
print(abs(5))

# bool() # True or / False
print(type(True))
print(type(False)) """

# all strings, numbers both positive and negative are True
# 0, empty list, empty set, empty dictionary, empty tuple, None, ''

""" print((bool(True)))
print((bool(False)))
print((bool('somestrings')))
print((bool(1)))
print((bool(-1)))
print('what is falsy value')
print((bool(False)))
print((bool(0)))
print((bool([])))
print((bool(())))
print((bool(set())))
print((bool({})))
print((bool('')))
print((bool(None))) """

countries = ['Finland', 'Sweden','Denmark','Norway','Iceland']
cities = ['Helsink', 'Stockholm', 'Copenhagen', 'Oslo', 'Reykjavík']
# cities = ['Helsink', 'Stockholm', 'Copenhagen', 'Oslo', 'Reykjavík']
# = ['FIN', 'SWE','DEN','NOR','ICE']
print(list(enumerate(countries)))
# for country in countries:
#     print(country)

for i,country in enumerate(countries):
    print(i + 1, country)

print(list(map(lambda x: [x, x.upper(), x.upper()[:3]], countries)))

print(list(filter(lambda x: 'land' in x, countries)))
print(list(filter(lambda x: 'land' not in x, countries)))

print(id(1))
print(id(2))
for i in range(10):
    print(id(i))

# sort and sorted

nums = [4, 2, 5, 3, 2, 6, -3, 5]

""" nums2 = nums.copy()
nums2.sort()
# mutation -> 
print(nums)
print(nums2) """

sorted_nums = sorted(nums)
print(nums)
print(sorted_nums)
print(countries + cities)
print(zip(countries, cities))
print(list(zip(countries, cities)))
for index, item in enumerate(zip(countries, cities)):
    print(index + 1, item[0], item[1])

# what ever u want to say
""" 
multiline 
can be written
like this

"""

'''
 this way is 
also posible
 '''
 # Data type: number(int, float, complex), boolean, String, List, Set, Tuple, Dictionary

print(type(10))
print(type(9.81))
print(type(1 + 4j))
print(type(True))
print(type(False))


def gen_user_id(length  = 6):
    alphabet = 'abacedefghijklmnopqrstuvwxyzACBCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    user_id = ''
    for l in range(length):
        index = random.randint(0, len(alphabet)-1)
        user_id = user_id + alphabet[index]
    return user_id

print(gen_user_id())
print(gen_user_id(3))
print(gen_user_id(32))



is_light_on = True
is_raining  = False
is_married = True
value = 4 > 2
lst = [1, 2, 3, 4]
names = ['Donald','Barack','Joe','Bill']
set_nums = {1, 2, 3, 4}
tpl = (1, 2, 3, 4)

user = {
    'firstname':'asab',
    'lastname':'yeta',
    'age':250,
    'country':'Finland',
    'city':'Helsinki',
    'is_married':True,
    'skills':['HTML','CSS','JS','Python'],
    'address':{
        'streetname':'spacestreet',
        'zipcode':'02270'
    }

}

a = 3
b = 4
c = 1 + 2j
d = 9.81

# +, - * / // % **

""" print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')

print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} // {b} = {a // b}')
print(f'{b} // {a} = {b // a}')
print(f'{b} % {a} = {b % a}')
print(f'{b} ** {a} = {b ** a}')
name = input('Entr you name')
print(name) """

country = 'Finland is beautiful'
print(country.upper())
print(country.lower())
print(country.title())
print(country.swapcase())
print(country.startswith('Fin'))
print(country.endswith('ful'))

a = -5
if a > 0:
    print('Positive')
elif a == 0:
    print('Zero')
elif a < 0:
    print('Negative')
else:
    print('Not a number')

value = 'positive value' if a > 0 else 'negative value'
print(value)

# while loop and for loop

lst = range(3)  # (0, 3)
print(list(lst))

for i in range(0, 101, 2):
    print(i)

for i in range(1, 101, 2):
    print(i)

def sum_of_all(n):
    total = 0
    for i in range(1,n+1, 2):
        total = total + i
    return total

print(sum_of_all(100))

""" k = 0

while k < 101:
    k = k + 1
    if k % 5 == 0 and k % 11 == 0:
            continue
    print(k) """
  
for i in range(11):
    if i == 5:
        continue
    print(i)
    
# Variables
# Operators
# Data types
# Builtin and custom
# List, set, tuple, dictionary
# Loops
# conditionals
# Functions
 
