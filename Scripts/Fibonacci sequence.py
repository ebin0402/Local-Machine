#Fibonacci sequence
'''
f,s=0,1
t=()
length=input("enter the length of sequence: ")
sequence=[0,1]
for item in range (int(length)):    
    t=f+s
    f,s=s,t
    sequence.append(t)
print(sequence)
'''
def main():
    f,s=0,1
    t=()
    length=input()
    sequence=[0,1]
    for item in range (int(length)-2):
        t=f+s
        f,s=s,t
        sequence.append(t)
    print(*sequence,sep=' ',end='')

 # Write code here 

main()


    
