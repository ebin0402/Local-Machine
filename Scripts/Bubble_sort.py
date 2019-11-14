#Bubble sort
lst=[]
swapped=True
n=int(input("How many elements? "))
for item in range(n):
    l=input("Enter elements: ")
    lst.append(l)
print("Entered list is: ",*lst)
while swapped:
    swapped=False
    for item in range(len(lst)-1):
        if lst[item]>lst[item+1]:
            swapped =True
            lst[item],lst[item+1]=lst[item+1],lst[item]
print("Sorted list is: ",*lst)

