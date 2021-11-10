nums = [1, 2, 3, 4] # [2, 4, 6, 8]

new_nums = []
for n in nums:
    new_nums.append(n * 2)
print(new_nums)

print([n * 2 for n in nums])

countries = ['Finland','Sweden','Norway']

list_list = [[c.upper(), c.upper()[:3], len(c)] for c in countries]
print(list_list)

integers = list(range(-10, 11))
print(integers)

# map, filter
postive_integers = [ i for i in integers if i > 0]
print(postive_integers)

negative_integers = [ i for i in integers if i < 0]
print(negative_integers)

postive_even_integers= [i for i in integers if i > 0 and i % 2 == 0]
print(postive_even_integers)