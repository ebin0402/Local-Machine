#Second Largest Number
'''length = input("How many numbers? ")
numb=[]
for item in range(int(length)):
    numbers=input("Enter the numbers: ")
    numb.append(numbers)
print(numb)
print(max(numb))
numb.remove(max(numb))
print(numb)
print("runner up  is ",max(numb))
'''
#Alternate

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])



