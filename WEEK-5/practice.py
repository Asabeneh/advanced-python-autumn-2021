
def addTwo(a, b):
    return a  + b




def sum_all_nums(*args):
    from functools import reduce
    return reduce(lambda x, y: x + y, args)

print(sum_all_nums(1, 2, 3, 5, 6, 1000))


def create_list_evens(n):
    return [i for i in range(0, n + 1, 2)]
 
print(create_list_evens(100))

# How you name your variables and functions
# purity of the function
# 