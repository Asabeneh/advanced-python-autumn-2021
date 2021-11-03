import re

""" re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string """

pattern = r'Love'
string = 'love is great'
match = re.match(pattern, string, re.I)
print(match)
if match:
    print(dir(match))
    print(match.start())
    print(match.span())
    start, end = match.span()
    print(string[end + 1:])

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend Python for a first programming language. JavaScript is also a great lanaguage, learn javaScript and make all websites more interactive than ever before.'''

match = re.search(r'Python', txt, re.I)
print(match)

print(re.findall(r'[pP]ython|[jJ]ava[S]cript',txt))
print(re.split(r'Python', txt))

print(re.sub(r'Python','JavaScript', txt, re.I))


txt = '''%I@ @a%m #te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%chin^g m%ore i%n%t%er%%es%ting? t%h%a!n an@y ot?her %jobs. 
D%o%es t;hi%s m%ot%i$v%a%te %y%o%u to b%e a t%e%a%cher?'''

print(re.sub(r'[^a-zA-Z ]+', '', txt))