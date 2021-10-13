# If a function takes another function as a parameter we call it a Higher Order Function(HOF)
# If a function return another function as a value we call a Higher Order Function(HOF)

def make_square(n):
    return n * n

print(make_square(2))
print(make_square(3))
print(make_square(10))

def make_cube(func, n):
    return func(n) * n

print(make_cube(make_square, 2))
print(make_cube(make_square, 3))
print(make_cube(make_square, 10))

def print_fullname (firstname, lastname):
    return firstname + ' ' + lastname

def get_person_info(func, firstname, lastname, age, country, skills):
    fullname = func(firstname, lastname)
    return f'I am {fullname}. I am {age} years old. I live in {country}. I have these skills such as {", ".join(skills)}'

print(get_person_info(print_fullname, 'Asabeneh','Yetayeh', 250, 'Finland',['HTML','CSS' ,'JS','Python'] ))


print(', '.join(['Finland','Sweden','Denmark','Norway']))

def some_hof():
    def do_something():
        return 'do somehting'
    return do_something

print(some_hof()())

def do_some_math(n):
    def add_ten():
        return n + 10
    return add_ten

print(do_some_math(10))
print(do_some_math(5))

def do_math(a, b):
    def add_nums():
        return a  + b
    def difference():
        return a - b
    def multiply():
        return a * b
    return {
        'add_nums':add_nums(),
        'difference':difference(),
        'multiply':multiply()
    }
print(do_math(1,4)['add_nums'])
# print(do_math()['difference'](100, 1))
# print(do_math()['multiply'](10, 4))
    
    
# map, filter, reduce 
# Pure and Impure Function
make_square(2)