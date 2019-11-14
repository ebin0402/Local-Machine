#WIN or LOSE
'''T=int(input("Enter the trials: "))
N=int(input("Participants: "))

def Fight():
    villain=[]
    player=[]
    for item in range(N):
        v=input("Enter Villains: ")
        villain.append(v)
    for item in range(N):
        p=input("Enter Players: ")
        player.append(p)
    for player in player:
        for villain in villain:
            if player>villain:
                status=True
            else:
                status=False
                break
    if status:
        print('WIN')
    else:
        print('LOSE')


for item in range(T):
    Fight()
'''
    
'''
a=[500,789,234,400,452,150]
b=[112,243,512,343,90,478]
a.sort()
b.sort()
print(a)
print(b)
if a>b:
    print('Success')
else:
    print('failure')
'''    


T=int(input())
def fight():
    players=[]
    villains=[]
    N=int(input())
    for item in range(N):
        p=input()
        players.append(p)
    for item in range(N):
        v=input()
        villains.append(v)
    players.sort()
    villains.sort()
    if players>villains:
        print('WIN')
    else:
        print('LOSE')
      
for item in range(T):
    fight()
    

    


