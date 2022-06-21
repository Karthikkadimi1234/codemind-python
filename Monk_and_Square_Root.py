t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=[]
    for j in range(0,b):
        d=j*j
        if d%b==a:
            c.append(j)
    if c==[]:
        print(-1)
    else:
        print(min(c))