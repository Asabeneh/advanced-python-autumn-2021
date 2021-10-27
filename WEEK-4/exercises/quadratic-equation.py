paragraph = 'I love teaching. If you do not love teaching, what else can you love. I love JavaScript if you do not love something ? which can give life to your application what else can you love.'
# print(count_words(paragraph,'love'))
# 6

text = '''
Congratulations on deciding to participate in 30 days of JavaScript programming challenge. In this challenge you will learn everything you need to be a JavaScript programmer, and in general, the whole concept of programming. In the end of the challenge you will get a 30DaysOfJavaScript programming challenge completion certificate. In case you need help or if you would like to help others you may join the telegram group.

A 30DaysOfJavaScript challenge is a guide for both beginners and advanced JavaScript developers. Welcome to JavaScript. JavaScript is the language of the web. I enjoy using and teaching JavaScript and I hope you will do so too.

In this step by step JavaScript challenge, you will learn JavaScript, the most popular programming language in the history of mankind. JavaScript is used to add interactivity to websites, to develop mobile apps, desktop applications, games and nowadays JavaScript can be used for machine learning and AI. JavaScript (JS) has increased in popularity in recent years and has been the leading programming language for six consecutive years and is the most used programming language on Github.

'''
def count_words (string, target):
    import re
    cleaned_text = re.sub('[^a-zA-Z ]', '', string)
    words = cleaned_text.lower().split()
    count = 0
    for word in words:
        if word == target.lower():
            count  = count + 1
    return count

print(count_words(paragraph, 'you'))
print(count_words(text, 'javascript'))

