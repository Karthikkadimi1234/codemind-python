n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i==a.count(i):
        b.append(i)
if b==[]:
    print("-1")
else:
    print(min(b),max(b),end=' ')