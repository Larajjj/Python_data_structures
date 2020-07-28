# LOOPING THROUGH STRINGS
# 1. Indeterminant loop
fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1


# 2. Determinant loop
fruit='banana'
for letter in fruit:
    print(letter)


# Counting the letter 'a' in banana
word='banana'
count=0
for letter in word:
    if letter== 'a':
        count=count+1
print(count) 


# String concatenation -> '+'
# String comparison    -> '==' '<' '>'


# String library
greet='HELLO'
zap= greet.lower()
print(zap)


# # Parsing and extracting
data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
spos=data.find(' ', atpos)
print(spos)
host=data[atpos+1 : spos]
print(host)


x='From marquard@uct.ac.za'
print(x[14:17])


print(len('banana')*7)


data='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos=data.find('.')
print(data[pos:pos+3])