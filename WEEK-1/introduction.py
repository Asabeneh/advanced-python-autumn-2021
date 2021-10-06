print('Hello')
print('Hello','World', 2021, 'I love Pyton')

# comment
# what is the pupose of a comment ?
# it allows us to leave some remark about the code ?
# it makes code more readable, clean, reusable

'''
the function below is print
it is a builtin function it takes unlimited number of arguments
'''
"""
this is 
a mulitiline
comment
"""

print(1, 2, 3, 4, 'WAHT EVER', True, [1, 2, 3], None, ('year', 2021))


# List comprehension can replace map and filter

countries = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
uppercase = [c.uppercase() for c in countries]
countries_with_land = [c.uppercase() for c in countries if 'land' in c]
country_codes = [[c, c.uppercase()[:3]] for c in countries]
