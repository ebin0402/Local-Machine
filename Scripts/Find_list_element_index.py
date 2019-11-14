#Find Element index from list
lst=[]
n=int(input("How many elements? "))
element=input("Which elment do you want to find? ")
found=False
for i in range(n):
    l=input("Enter Element: ")
    lst.append(l)
for item in lst:
    if item==element:
        found=True
        break
if found:
    print("The element: ",item," is located at ",lst.index(item))
else:
    print("Not Found!!!!")
    


        
