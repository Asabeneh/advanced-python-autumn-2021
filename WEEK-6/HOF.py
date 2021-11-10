def make_square(n):
    return n ** 2

def make_cube(func, n):
    return func(n) * n

print(make_cube(make_square, 2))
print(make_cube(make_square, 3))
print(make_cube(make_square, 10))

def do_something(n):
    def add_ten():
        return n + 10
    return add_ten
print(do_something(5)())
print(do_something(10)())