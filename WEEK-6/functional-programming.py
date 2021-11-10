# map, filter, reduce

nums = [1, 2, 3, 4] #[1, 4, 9, 16]
nums_squared = list(map(lambda n: n ** 2, nums))
print(nums_squared)

countries = ['Finland','Sweden','Norway','Denmark','Iceland']
countries_with_land = list(filter(lambda c: 'land' in c, countries))
print(countries_with_land)

from functools import reduce
total = reduce(lambda x, y: x + y, nums)
print(total)



