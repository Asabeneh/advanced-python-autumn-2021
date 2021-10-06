# Function: Function is a block of code that perform a certain task. 
# It can be reuse
# builtin functions
# custom functions
from pprint import pprint

""" print('hi','i love py', 2021)
print(max(1, 2, 10, -10))
print(min(1, 2, 10, -10))
print(sum([1, 2, 10, -10])) """


""" def print_fullname(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name
    
print(print_fullname('Asabeneh','Yetayeh'))
print(print_fullname('Donald','Trump'))
print(print_fullname('Bill','Gates'))
print(print_fullname('Steve', 'Jobs')) """

""" def add_two_nums(a, b):
    total = a  + b
    return total

print(add_two_nums(1, 2))
print(add_two_nums(1, 9))

# a function that adds from 0 to n

def sum_all_nums(n):
    total = 0
    for i in range(n + 1):
        total = total + i
    return total
print(sum_all_nums(3)) # 0, 1, 2, 3
print(sum_all_nums(10)) 
print(sum_all_nums(100))


def sum_evens(n):
    total = 0
    for i in range(0, n + 1, 2):
        total = total + i
    return total


print(sum_evens(3))  # 0, 1, 2, 3
print(sum_evens(10)) # 0, 2, 4, 6, 8, 10
print(sum_evens(100))

countries = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh','Donald','Bill','Steve']

def change_list_touppercase(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item.upper())
    return new_lst

print(change_list_touppercase(countries))
print(change_list_touppercase(names))

def make_square (n):
    return n ** 2

print(make_square(2))
print(make_square(3))
print(make_square(11))

for i in range(11):
    print(make_square(i))

# weight of abody on a planet
def calculate_weight(mass, gravity = 9.81):
    weight = mass * gravity
    return weight

print(calculate_weight(75))
print(round(calculate_weight(75, 1.62), 1)) """

# def generate_random_id():
letters = 'abcedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def generate_random_user_id(n = 6):
    import random
    random_id = ''
    for i in range(n):
        index = random.randint(0, len(letters) - 1)
        random_id = random_id + letters[index]

    return random_id
print(generate_random_user_id(32))
print(generate_random_user_id(24))
print(generate_random_user_id())

# Functions that take arbitrary number of arguments
# * allows as to pack the arguments to a tuple
def sum_numbers(*args):
    total = 0
    for i in args:
        total +=  i
    return total
print(sum_numbers(-100, 250, 300, -50, 1, 2, 3, 4))

def get_person_info(**params):
    pprint(params)


## ** allows to pack the arguments to dictionary
get_person_info(first_name='Asabeneh', 
last_name='Yetayeh', 
age = 250, 
skills=['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
is_married = True,
address = {
    'street': 'Space street',
        'zipcode': '02210'
}
)
# Lets talk about lambda function
# Annonymous function

lambda_func = lambda x, y : x ** 2 + x * y + 10
print(lambda_func(3, 2))

