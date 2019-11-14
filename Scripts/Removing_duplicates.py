lst1=[]
for i in range(10):
    lst1.append(input("Enter the list: "))
print("Entered values are: ",lst1)
unique=[]
for item in lst1:
    if item not in unique:
        unique.append(item)
unique.sort()
print("Unique list is: ",unique)
