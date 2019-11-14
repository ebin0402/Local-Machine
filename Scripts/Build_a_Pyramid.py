#Build_a_Pyramid
blocks=int(input("How many blocks?: "))
height=0
base=1
for stones in range(blocks):
    base+=1
    height+=1
    if base>blocks:
        break
    else:
        continue
print(height)

    
           
