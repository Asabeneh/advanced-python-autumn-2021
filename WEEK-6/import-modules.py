""" import pprint
from pprint import pprint as pretty_print
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'country':'Finland',
   'age': 250,
    'skills':['HTML','CSS','JS'],
    'is_married':True,
    'address':{
        'city':'Helsinki',
        'street_name':'Space Street',
        'zipcode':'0200'
    }
}

pretty_print(person) """

from math import sqrt, ceil, floor, pow, log10, log2

print(sqrt(9))
print(sqrt(2))
print(2 ** 0.5 )
print(9 ** 0.5)
print(ceil(9.81))
print(ceil(3.14))
print(floor(9.81))
print(pow(2, 2))
print(pow(2, 10))
print(log10(10))
print(log10(100))