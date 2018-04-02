t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=[int(i) for i in input().split()]
    cont=0
    for j in l:
        if(j<=0):
            cont +=1
    if cont<k:
        print("YES")
    else:
        print("NO")
    l=[]