n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i==a.count(i) and i not in b:
        b.append(i)
if b==[]:
    print(-1)
else:
    print(*b)