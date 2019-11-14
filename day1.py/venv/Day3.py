#FOR LOOPS

'''for  item in range(15,80,5):
    print(item)
'''

#Problem: Calculate the total cost of all items ina shopping cart
#Soln:
'''prices =[10,15,25,50]
total =0
for item in prices:
    total=total+item
print(f"Toatal: {total}")#formattes string
'''

#NESTED LOOPS
#Program to generate coordinates

'''for x in range(4,10,2):
    for y in range(3,10,3):
        print(f'({x} , {y})')
'''

#CHALLENGE
#Draw an F shape with nested loops
'''for example
xxxxx
xx
xxxxx
xx
xx

'''
'''Design=[5,2,5,2,2]
for item in Design:
    print('x'*item)
'''
'''
numbers = [5,2,5,2,2]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output+='*'
    print(output)
'''



