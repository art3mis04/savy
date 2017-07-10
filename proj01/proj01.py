# Name: Caroline Duncan
# Date: July 9, 2017

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.
x=raw_input('enter your name: ')
y=raw_input('enter your age: ')
b= raw_input('have you had your birthday this year? ')
y=int(y)
z= 2017 - y
if b=="no":
    z=z-1
w=z+100
my_str= x
x=my_str[0]
x=x.upper()
a=my_str.lower()
a=end_slice=my_str[1:]
if y>=100:
    print (x+a),("you were 100 in the year"),w
print (x+a),('you will be 100 in the year'),w
print(x+a),('you can watch g and pg movies')
if y<=13:
    print(x+a),('you can watch pg-13 movies')
if y>=17:
    print(x+a),('you can watch R movies')
if len(x+a) >= 5:
    print(x+a),('you have more than 5 letters in your name')






# If you complete extensions, describe your extensions here!


