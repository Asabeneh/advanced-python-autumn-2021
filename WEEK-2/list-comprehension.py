# allows to write a clean and short code
# it faster than regular loop
from pprint import pprint
nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]

""" List comprehension """

new_lst = [ num ** 2 for num in nums]
evens = [num  for num in nums if num % 2 == 0]

print(new_lst)
print(evens)

""" new_nums = []
for num in nums:
    new_nums.append(num ** 2)

print(new_nums) """

""" def make_square(n):
    return n ** 2
def map_list(lst):
    new_lst = []
    for item in lst:
        new_lst.append(make_square(item))
    return new_lst
print(map_list(nums)) """

countries = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']


uppercase = [c.upper() for c in countries]
print(uppercase)
lst_lst = [[c, c.upper(), c.upper()[:3], len(c)] for c in countries]
pprint(lst_lst)

countries_with_land = [c for c in countries if 'land' in c]
print(countries_with_land)
countries_with_way = [c for c in countries if 'way' not in c]
print(countries_with_way)

nums = list(range(101))
print(nums)
evens = list(range(0, 101, 2))
print(evens)

odds = list(range(1, 101, 2))
print(odds)
