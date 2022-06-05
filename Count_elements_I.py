n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=set(a)
d=set(b)
e=0
for i in c:
    for j in d:
        if i==j:
            e+=1
print(e)
