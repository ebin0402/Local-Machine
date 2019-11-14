#LISTS

'''names=['Ebin','Baby','Sibin','Ribin','Alice']
print(names[:])
names[0]='Eby'
print(names)
'''

#EXERCISE
#Write a program to find the largest number in the list

'''numbers=[1,2,3,6,5,4,7,8,9,6,65,3,2,888,569,78932589,5,0,-5,-986,-2]
print(numbers)
print(max(numbers))
print(min(numbers))

min=numbers[0]
for number in numbers:
    if number < min:
        min=number
print(min)


max=numbers[0]
for number in numbers:
    if number > max:
        max=number
print(max)
'''

#2D LISTS

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print(matrix[1][1])
matrix[1][1]*=100
print(matrix[1][1])
print(matrix)

for item in matrix:
    for row in item:
        print(row)