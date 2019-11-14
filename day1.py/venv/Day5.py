#LIST METHODS
# numbers=[1,2,3,4,5,6,7,5,-1,0,99,89]
# numbers2=numbers.copy()
# print(numbers.index(5))
# numbers.append(20)
# print(numbers)
# numbers.insert(0,200)
# print(numbers)
# numbers.remove(7)
# print(numbers)
# print(numbers[3])
# numbers.pop()
# print(numbers)
# #numbers.clear()
# #print(numbers)
# print(5 in numbers)
# print(numbers.count(5))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
#
# print(numbers2)

#EXERCISE: Write a Program to remove the duplicates in a List

#Solution


#TUPLES
# numbers=(1,2,3,4,5,66,7,7,4)
# print(numbers)
# # numbers.append(12)#AttributeError: 'tuple' object has no attribute 'append'

#UNPACKING
# coordinates=(1,2,3)#This feature can be used for Lists as well
# x,y,z=coordinates
# print(x)
# print(y)
# print(z)

# DICTIONARIES
# n=[]
# ag=[]
# for i in range(1):
#     name=input("Enter the name: ")
#     n.append(name)
#     age=input("Enter the age: ")
#     ag.append(age)
#
# User_data={
#     "Name1": n,
#     "Age": ag
# }
# print(User_data["Name1"])
# print(User_data.get(name,'Baby'))#get() methon can be used to customise the exception whil accessing valued in a dictionary

#EXERCISE -- write a program that takes in numbers like 1,2,3 and prints the output in words (one, two, three)
# num_to_word={
#     '1':"One",
#     '2':"Two",
#     '3':"Three",
#     '4':"Four",
#     '5':"Five",
#     '6':"Six",
#     '7':"Seven",
#     '8':"Eight",
#     '9':"Nine",
#     '0':"Zero"
# }
# user_input=(input("Enter the Number(0 -9): "))
# for item in user_input:
#     print(num_to_word.get(item,'!'),'\t', end='')


#EMOJI CONVERTER
# Import QRCode from pyqrcode
import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "www.google.com"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("myqr.svg", scale=8)
