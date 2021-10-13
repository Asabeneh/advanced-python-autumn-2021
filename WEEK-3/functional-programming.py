# map, filter, reduce
from pprint import pprint
nums = [1, 2, 3, 4, 5]  # [1, 4, 6, 8, 10]
""" 
new_nums = []
for n in nums:
    new_nums.append([n, n * 2, n ** 2, n ** 3])

pprint(new_nums) """

new_nums = [[n, n * 2, n ** 2, n ** 3] for n in nums]
print(new_nums)

countries = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
new_countries = [[c, c.upper(), c.upper()[:3], len(c)] for c in countries]
print(new_countries)

value = lambda x, y: x ** 2 + 2 * x * y + 10
print(value(2, 3)) # 4 + 12 +10 = 26


new_list = map(lambda x : [x, x *2, x ** 2, x ** 3],  nums)
print(list(new_list))

new_countries_list = map(lambda c: [c, c.upper(), c.upper()[:3]], countries)
print(list(new_countries_list))

""" # Filter
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)

# Filter
odds = []
for n in nums:
    if n % 2 != 0:
        odds.append(n)
print(odds) """


""" evens = [n for n in nums if n % 2 == 0]
odds= [n for n in nums if n % 2 != 0]
print(evens, odds) """

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)

countries_with_land = list(filter(lambda c: 'land' in c, countries))
print(countries_with_land)

countries_without_land = list(filter(lambda c: 'land' not in c, countries))
print(countries_without_land)

# reduce 
from functools import reduce

total = reduce(lambda acc, cur: acc + cur, nums)
print(total)

product = reduce(lambda acc, cur: acc * cur, nums)
print(product)


