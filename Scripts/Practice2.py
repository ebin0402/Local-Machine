input1=input("Enter the list: ")
itr=len(input1)
f=[]
x=1
for i in range(itr-1):
    for item in input1:
        if item != input1[x]:
            f.append(item)
            x+=1
print(f)


        



        
    
