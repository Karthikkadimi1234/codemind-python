t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    k=sorted(a)
    
    if k!=a:
        print(max(a)-min(a))
    else:
        print(0)