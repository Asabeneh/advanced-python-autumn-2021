from functools import reduce

sentences = ['The Deep Learning textbook is a resource intended to help students and practitioners enter the field of machine learning in general and deep learning in particular. ', 'learning is great'] 

""" word_count = reduce(lambda x, y: (x + y).count("learning"),sentences,0) """

""" print('learning:', word_count)  # 2

print('The Deep Learning textbook is a resource intended to help students and practitioners enter the field of machine learning in general and deep learning in particular. '.count('learning')) """

# reduce(lambda x, y: print(x, y),sentences,0) 
print(reduce(lambda x, y: x + y.count("learning"),sentences,0))

loves = [
    'I love people',
    'I love everyone',
    'love is great, because it is love'
]
def call_back(x, y):
    print('x:', x, 'y:', y.count('love'))
    return x + y.count("love")
    
print(reduce(call_back,loves,0))