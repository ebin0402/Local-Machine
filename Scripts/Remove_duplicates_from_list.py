#Remove duplicates from a list
n=int(input("How many elements: "))
lst=[]
unique=[]
for i in range(n):
    l=input("Enter element: ")
    lst.append(l)
print("List is : ",*lst)
for item in lst:
    if item not in unique:
        unique.append(item)
lst=unique[:]
print("Unique list is: ",*lst)


    
