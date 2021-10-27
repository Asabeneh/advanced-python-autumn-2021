# string = ''
# for i in range(len('hello'), ):
#     print('hello'[i])

# for x in range(2, -1, -1):
#     print(x)



print(list(range(0, 101)))

evens = list(range(0, 101, 2))
print(evens)
odds = list(range(1, 101, 2))
print(odds)

print(list(range(10, -1, -1)))



def reverse_word(word):
    reversed_word = ''
    for i in range(len(word)-1, -1, -1):
        reversed_word = reversed_word + word[i]
    return reversed_word
print(reverse_word('Hello'))
print(reverse_word('Book'))


# Write a function that return list of palindrome words from the given string.

def find_list_palindrom(string):
    return []



""" def reverse_word (word):
    return word[::-1]
 """

""" def reverse_word (word):
    word = list(word)
    word.reverse()
    return ''.join(word)

print(reverse_word('Asab')) """

""" def reverse_word(word):
    reversed_word = ''
    for i in range(len(word)-1, -1, -1):
        reversed_word = reversed_word + word[i]
    return reversed_word """