import random
d1 = [1,2,3,4,5,6]
d2 = [1,2,3,4,5,6]
d=[]
for i in d1:
    for j in d2:
        d.append([i,j])
    print(d)
di={}
for i  in range(2,13):
    c = 0
    for j in d:
        if i == j[0] + j[1]:
            c += 1
        di[str(i)] = c/len(d)
    print(di) 
p = int(input())   
p1 = [[1,2], [3,4]]
p2 = [[1,3],[5,6]] 
for key, value in di.items():
    if str(sum(p1)) == key:
        p1 = value
    

r=int(input("enter the r value:"))
a=[]
player1=player2=0
for i in range(1,7):
    for j in range(1,7):
        a.append([i,j])
k={}

for i in range(len(a)):
    if sum(a[i]) not in k:
        k[sum(a[i])]=1
    else:
        k[sum(a[i])]+=1

for i in range(r):
    a,b,c,d=map(int,input().split())

    if k[a+b]/36<k[c+d]/36:
        player1+=1
    else:
        player2+=1


        
if player1>player2:
    print("player1 wins")
elif player1<player2:
    print("player2 wins")
else:
    print("draw")
