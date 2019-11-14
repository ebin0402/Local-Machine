'''name=input('Enter your name : ')
age=input('How old are you? ')

print('hello ',name,' you are ',age ,' years old!!')
'''
'''
#Formatted Strings
first ='Ebin'
last ='Baby'
#message =first,'[' ,last,' ] is a Coder'
msg =f'{first} [{last}] is a coder'#this is a formatted string. a formatted string will be prefixed with an f
print(msg)
'''
'''
# STRING METHODS
#diff between function and a method -- When a function belongs to something else or specific to some kind of an object, that function is called as a method
course ='Python for Beginners'
print(len(course))# here print and len are fuctions and upper is a method as it belongs to strings
print(course.upper())
print(course)
print(course.lower())
print(course.find('b'))# this returns the index of firstoccurence of the character
print(course.replace('B','b'))# to replace the characters or strings
print('python' in course)# checks if the passed value is present in the variable-- out will be a boolean value
'''

#ARITHMETIC OPERATIONS
#Operations : +, -, /, //, *, **, %


#OPERATOR PRECEDENCE
'''
Order:
1. Exponentiation
2. Multiplication or division
3. addition or substraction
Paranthesys  can be uded to change the priority***
'''

'''
#MATH FUNCTIONS
print(round(8.999))
print(abs(-8326))

#To perform complicated mathematical calculations, Math module can be imported
import math # google the python 3 math module documentation
print(math.ceil(3.2))
'''


#IF STATEMENTS
'''is_hot=False
is_cold=False
if is_hot:
    print("it's a hot day")
    print('Drink pleanty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print("Enjoy your day")
'''
'''
Exercise
Problem: Price of a house is $1M, If a buyer has good credit, they need to put down 10%
otherwise
they need to put down 20%
print the down payment
'''

'''price=1000000
is_good_credit=False

if is_good_credit:
    down=(10/100)*price
else:
    down=(20/100)*price

print(f"Yo need to pay ${down}")
'''

#LOGICAL OPERATORS
'''
has_high_income=False
has_good_credit=True

if has_high_income or has_good_credit:
    print('Eligible for loan')
'''

#COMPARISON OPERATION
'''temp=35
if temp>30:
    print('It is a hot day')
else:
    print("it's not a hot day")
# >, >=, <, <=, ==, !=
'''
#Exercise
'''
If a name is less than 3 charcters long: name must be atleast 3 charters long
if it is more than 50 characters long: Name can be max of 50 characters
othervise: Name looks good
'''
#Solution
'''
name = input("What is your name? ")
if len(name)<3:
    print("Name should be atleast 3 charcters")
elif len(name)>50:
    print("Name should be of Maximun 50 Characters")
else:
    print(name," Your name is awsome")
'''

''''#PROJECT WEIGHT CONVERTER
weight=int(input('Weight : '))
unit=input('(L)lbs or (K)g: ')
if unit.upper()=='K':
    print ("you are ", float(weight)*2.2, "Pounds")
elif unit.upper()=='L':
    print ('you are ',float(weight)/2.2,' Kilos')
'''




