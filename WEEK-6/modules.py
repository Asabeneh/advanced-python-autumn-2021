# to make our code reusable
# maintable
# testable

def make_square(n):
    return n ** 2
def double_number(n):
    return n * 2
def add_two_numbers(a, b):
    return a + b
def calc_weight(mass, gravity = 9.81):
    return mass * gravity
def add_numbers(*args):
    from functools import reduce
    return reduce(lambda x, y : x + y, args)

def check_datatypes(lst, t):
    count = 0
    for item in lst:
        if type(item) == t:
            count += 1
    if count == len(lst):
        return True
    return False



        
    
