# 

""" for i in range(101):
    print(f'{i} * {i} = {i * i}')
     """
   
i = 0  
while i < 101:
    print(f'{i} * {i} = {i * i}')
    i += 1

countries = ['Finland','Sweden','Norway']
new_list = []
for c in countries:
    new_list.append([c.upper(), c.upper()[:3], len(c)])
print(new_list)